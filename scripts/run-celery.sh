#!/bin/sh

set -e

# Go to backend folder
cd $(dirname $0)/../src

# Variables
DJANGO_PROJECT_NAME="diagnosis"
DEVELOPMENT_SETTINGS="diagnosis.settings.development"
PRODUCTION_SETTINGS="diagnosis.settings.production"


if [ "$1" = "--dev" ];
    then
    echo "running celery with development settings"
        DJANGO_SETTINGS_MODULE=${DEVELOPMENT_SETTINGS} \
            celery -A ${DJANGO_PROJECT_NAME} \
                worker -l info

elif [ "$1" = "--prod" ];
    then

    echo "running celery with production settings"
        DJANGO_SETTINGS_MODULE=${PRODUCTION_SETTINGS} \
            celery -A ${DJANGO_PROJECT_NAME} \
                worker -l info

else
echo "Error: runtime not selected. Please add exactly one runtime flag
to select a runtime for the app.
options:
    --dev: for a development runtime
    --prod: for a production runtime 
 "
    exit 128
fi
