#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/Users/prathyusha/Documents/job-hunter-api'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart jobhunter_api

echo "DONE! :)"
