#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

ARGS="--check"

# call this script with --fix to have it fix the files
if [ "$1" = "--fix" ]; 
    then
        echo "Files will be formatted"
        ARGS=""
fi

poetry run black ${ARGS} src tests
