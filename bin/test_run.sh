#!/usr/bin/env bash
# owner @i.balagurov
# the script for running tests

echo "Run tests..."
poetry run pytest "$@"
echo "Tests running is done"
