#!/usr/bin/env bash
# owner @i.balagurov
# the script for autoformatting and checking code styles

echo "Run code formatter..."
poetry run black . --line-length "120" --target-version py37
echo "Code formatting is done"

echo "Run linter..."
poetry run flake8 .
echo "Linting is done!"
