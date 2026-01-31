#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE_NAME="furl-ai-exercise"

# Build the image
echo "Building Docker image..."
docker build -f "$SCRIPT_DIR/docker/Dockerfile" -t "$IMAGE_NAME" "$SCRIPT_DIR"

# Run with submission if provided, otherwise just run tests
if [ -n "$1" ]; then
    SUBMISSION_PATH="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
    echo "Running submission: $SUBMISSION_PATH"
    docker run --rm --env-file "$SCRIPT_DIR/.env" \
        -v "$SUBMISSION_PATH:/submissions/submission.zip:ro" \
        "$IMAGE_NAME" /submissions/submission.zip
else
    echo "Running base tests..."
    docker run --rm --env-file "$SCRIPT_DIR/.env" "$IMAGE_NAME"
fi
