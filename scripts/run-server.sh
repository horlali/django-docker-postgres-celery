#!/bin/sh

set -e

# Variables
NAME="Diagnosis-Backend-System"
PROJECT_DIR="${PWD}/src"
DJANGO_WSGI_MODULE="diagnosis.wsgi"
NUM_WORKERS=4
NUM_THREADS=4
TIMEOUT=1800
PORT=8000

# Project runtime and directory logic
if [ "$1" = "--docker" ];
    then
        echo "Container Directory: ${PROJECT_DIR}"
        HOST=0.0.0.0

elif [ "$1" = "--local" ];
    then
        echo "Local Directory: ${PROJECT_DIR}"
        HOST=127.0.0.1

else
echo "Error: runtime not selected. Please add exactly one runtime flag
to select a runtime for the app.
options:
    --local: for a local runtime
    --container: for docker runtime
 "
    exit 128
fi

# Server
if [ "$2" = "--dev" ];
    then
        echo "Starting Development Server with Django Server"
        
        # Django Settings
        export DJANGO_SETTINGS_MODULE=diagnosis.settings.development

        # Migrations
        python ${PROJECT_DIR}/manage.py makemigrations
        python ${PROJECT_DIR}/manage.py migrate

        # Load Staticfiles
        python ${PROJECT_DIR}/manage.py collectstatic --no-input

        # Starting Development Server
        python ${PROJECT_DIR}/manage.py runserver ${HOST}:${PORT}

elif [ "$2" = "--prod" ];
    then
        echo "Starting Production Server with Gunicorn Server"
        
        # Django Settings
        export DJANGO_SETTINGS_MODULE=diagnosis.settings.production

        # Migrations
        python ${PROJECT_DIR}/manage.py makemigrations
        python ${PROJECT_DIR}/manage.py migrate

        # Load Staticfiles
        python ${PROJECT_DIR}/manage.py collectstatic --no-input

        # # Starting Gunicorn server
        gunicorn ${DJANGO_WSGI_MODULE}:application \
            --name ${NAME} \
            --chdir ${PROJECT_DIR} \
            --bind=${HOST}:${PORT} \
            --workers ${NUM_WORKERS} \
            --timeout ${TIMEOUT} \
            --log-level=debug \
            --threads=${NUM_THREADS} \
            --worker-class=gevent

else
echo "Error: server not selected. Please add exactly one server flag
to select a runtime for the app.
options:
    --dev: for development server
    --prod: for production server
 "
    exit 128
fi

exec "$@"
