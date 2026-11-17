"""Write and consolidate Allure session metadata using the standard library."""

import argparse
import json
import os
import platform
import shutil
import tempfile
from pathlib import Path

CATEGORY_TEMPLATE = Path(__file__).resolve().parents[1] / "config" / "allure_categories.json"
MANIFEST = "execution-metadata.json"
GLOBAL_FILES = {"environment.properties", "categories.json", MANIFEST}
ALLOWED_KEYS = {
    "Environment", "Python", "OS", "Execution", "Container",
    "CI.Run.ID", "CI.Run.Attempt", "Browsers.Selected",
}


def runtime_metadata(environment, browsers):
    """Read only explicitly allowed, non-secret runtime values."""
    metadata = {
        "Environment": [environment],
        "Python": [platform.python_version()],
        "OS": [f"{platform.system()} {platform.release()}"],
        "Browsers.Selected": sorted(set(browsers)),
    }
    if os.environ.get("GITHUB_ACTIONS") == "true":
        metadata["Execution"] = ["GitHub Actions"]
        for variable, key in (
            ("GITHUB_RUN_ID", "CI.Run.ID"),
            ("GITHUB_RUN_ATTEMPT", "CI.Run.Attempt"),
        ):
            value = os.environ.get(variable, "")
            if value.isascii() and value.isdigit():
                metadata[key] = [value]
    if Path("/.dockerenv").is_file():
        metadata["Container"] = ["Docker"]
        metadata.setdefault("Execution", ["Docker"])
    return metadata


def _atomic_write(path, content):
    """Replace a complete file atomically on the same filesystem."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content.encode("utf-8"))
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def _properties_escape(value):
    """Escape Java Properties special characters and non-ASCII code units."""
    escaped = []
    for character in value:
        if character in "\\=:#! ":
            escaped.append("\\" + character)
        elif character == "\n":
            escaped.append("\\n")
        elif character == "\r":
            escaped.append("\\r")
        elif character == "\t":
            escaped.append("\\t")
        elif ord(character) < 32 or ord(character) > 126:
            encoded = character.encode("utf-16-be")
            escaped.extend(
                f"\\u{int.from_bytes(encoded[index:index + 2], 'big'):04x}"
                for index in range(0, len(encoded), 2)
            )
        else:
            escaped.append(character)
    return "".join(escaped)


def write_metadata(directory, metadata):
    """Write the same canonical metadata to Allure and the CI manifest."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    canonical = {
        key: sorted(set(values))
        for key, values in sorted(metadata.items())
        if key in ALLOWED_KEYS and values
    }
    properties = "".join(
        f"{key}={_properties_escape(', '.join(values))}\n"
        for key, values in canonical.items()
    )
    _atomic_write(directory / "environment.properties", properties)
    _atomic_write(directory / MANIFEST, json.dumps(canonical, indent=2) + "\n")
    _atomic_write(directory / "categories.json", CATEGORY_TEMPLATE.read_text(encoding="utf-8"))


def merge_results(source_root, destination):
    """Merge downloaded browser artifacts without last-writer-wins metadata."""
    source_root, destination = Path(source_root), Path(destination)
    sources = sorted(source_root.glob("playwright-results-*/allure-results"))
    if destination.exists() and any(destination.iterdir()):
        raise ValueError(f"Merge destination must be empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    combined = {}
    for source in sources:
        manifest = source / MANIFEST
        if manifest.is_file():
            metadata = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(metadata, dict):
                raise ValueError(f"Invalid metadata object: {manifest}")
            for key, values in metadata.items():
                if key not in ALLOWED_KEYS:
                    continue
                if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                    raise ValueError(f"Invalid metadata values: {manifest}: {key}")
                combined.setdefault(key, set()).update(values)
        else:
            print(f"WARNING: No execution metadata for {source.parent.name}")
        for source_file in sorted(source.iterdir()):
            if source_file.name in GLOBAL_FILES or not source_file.is_file():
                continue
            target = destination / source_file.name
            if target.exists():
                if source_file.read_bytes() != target.read_bytes():
                    raise ValueError(f"Conflicting Allure artifact: {source_file.name}")
            else:
                shutil.copy2(source_file, target)
    if not any(destination.glob("*-result.json")):
        raise ValueError("No Allure test results found")
    write_metadata(destination, combined)


def main():
    """Consolidate browser artifacts for the GitHub Actions report job."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    arguments = parser.parse_args()
    merge_results(arguments.source, arguments.destination)


if __name__ == "__main__":
    main()
