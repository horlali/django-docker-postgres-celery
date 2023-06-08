#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

# flake8 is silent when it's successful, so make some noise
poetry run flake8 src tests && echo "flake8 successful"
