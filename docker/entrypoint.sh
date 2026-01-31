#!/bin/bash
set -e

SUBMISSION_DIR="/app"

# Check if a zip file was provided as an argument
if [ -n "$1" ] && [ -f "$1" ]; then
    echo "Extracting submission from: $1"

    # Create temp directory for extraction
    TEMP_DIR=$(mktemp -d)
    unzip -q "$1" -d "$TEMP_DIR"

    # Find the root of the extracted content
    # Handle both flat zips and zips with a single root folder
    EXTRACTED_CONTENT=$(find "$TEMP_DIR" -mindepth 1 -maxdepth 1)
    NUM_ITEMS=$(echo "$EXTRACTED_CONTENT" | wc -l)

    if [ "$NUM_ITEMS" -eq 1 ] && [ -d "$EXTRACTED_CONTENT" ]; then
        # Single directory - use its contents
        SOURCE_DIR="$EXTRACTED_CONTENT"
    else
        # Multiple items or flat structure - use temp dir
        SOURCE_DIR="$TEMP_DIR"
    fi

    # Copy submission src files over the base (preserving tests from base image)
    if [ -d "$SOURCE_DIR/src" ]; then
        cp -r "$SOURCE_DIR/src/"* "$SUBMISSION_DIR/src/"
        echo "Copied src/ from submission"
    fi

    # Optionally copy tests if they exist in submission
    if [ -d "$SOURCE_DIR/tests" ]; then
        cp -r "$SOURCE_DIR/tests/"* "$SUBMISSION_DIR/tests/"
        echo "Copied tests/ from submission"
    fi

    # Copy pyproject.toml and poetry.lock if they exist
    if [ -f "$SOURCE_DIR/pyproject.toml" ]; then
        cp "$SOURCE_DIR/pyproject.toml" "$SUBMISSION_DIR/"
        echo "Copied pyproject.toml from submission"
    fi
    if [ -f "$SOURCE_DIR/poetry.lock" ]; then
        cp "$SOURCE_DIR/poetry.lock" "$SUBMISSION_DIR/"
        echo "Copied poetry.lock from submission"
    fi

    # Clean up
    rm -rf "$TEMP_DIR"

    # Install dependencies from submission
    echo "Installing dependencies..."
    poetry install --no-interaction --no-ansi

    echo "Running pytest on submission..."
    echo "================================"
    exec pytest "${@:2}"
else
    # No zip file - run pytest with any provided arguments
    exec pytest "$@"
fi
