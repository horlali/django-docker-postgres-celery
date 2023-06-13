#!/bin/sh

# Go to backend folder
cd $(dirname $0)/../src

celery -A diagnosis worker -l info
