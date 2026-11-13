pytest_plugins = [
    "fixtures.environment",
    "fixtures.pages",
    "fixtures.authentication",
]


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=["dev", "qa", "staging"],
        help="Execution environment",
    )