FROM mcr.microsoft.com/playwright/python:v1.64.1-noble

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTEST_ADDOPTS="-o cache_dir=/tmp/pytest-cache"

WORKDIR /app

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY config/ ./config/
COPY data/ ./data/
COPY fixtures/ ./fixtures/
COPY pages/ ./pages/
COPY resources/ ./resources/
COPY tests/ ./tests/
COPY utils/ ./utils/
COPY conftest.py pytest.ini ./

RUN mkdir -p reports test-results \
    && chown pwuser:pwuser reports test-results

USER pwuser

CMD ["python", "-m", "pytest"]
