#!/bin/sh

set -e

ARGS=""

if [ "$1" = "--fix" ]
    then
        echo "linters might modify files"
        ARGS="--fix"
fi

echo "======Black formatting checks======"
./scripts/run-black.sh ${ARGS}

echo "====Isort import sorting checks===="
./scripts/run-isort.sh ${ARGS}

echo "=======Flake8 linting checks======="
./scripts/run-flake8.sh
