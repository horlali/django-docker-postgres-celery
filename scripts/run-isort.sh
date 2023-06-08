#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

ARGS="--check-only"

# call this script with --fix to have it fix the files
if [ "$1" = "--fix" ];
    then
        echo "All files will have their imports sorted"
        ARGS=""
fi

poetry run isort ${ARGS} src tests && echo "isort successful"
