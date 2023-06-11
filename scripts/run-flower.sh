#!/bin/sh

# Go to backend folder
cd $(dirname $0)/../src

celery -A diagnosis --broker=redis://redis:6379 flower --port=5555
