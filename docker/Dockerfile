FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy dependency files first for better caching
COPY pyproject.toml poetry.lock ./

# Configure Poetry to not create a virtual environment (use system Python)
RUN poetry config virtualenvs.create false

# Install dependencies only (not the project itself)
RUN poetry install --no-interaction --no-ansi --no-root

# Copy source code and tests (base scaffold)
COPY src/ ./src/
COPY tests/ ./tests/

# Now install the project itself
RUN poetry install --no-interaction --no-ansi

# Copy entrypoint script
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create directory for mounting submissions
RUN mkdir -p /submissions

ENTRYPOINT ["/entrypoint.sh"]
