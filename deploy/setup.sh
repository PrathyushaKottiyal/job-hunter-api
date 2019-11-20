#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/PrathyushaKottiyal/job-hunter-api.git'

PROJECT_BASE_PATH='/Users/prathyusha/Documents/job-hunter-api'

echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Create project directory
sudo rm -rf $PROJECT_BASE_PATH
sudo mkdir -p $PROJECT_BASE_PATH
sudo git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
sudo mkdir -p $PROJECT_BASE_PATH/env
sudo python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
sudo -H $PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.text
sudo -H $PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
sudo $PROJECT_BASE_PATH/env/bin/python manage.py migrate
sudo $PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
sudo cp $PROJECT_BASE_PATH/deploy/supervisor_jobhunter_api.conf /etc/supervisor/conf.d/jobhunter_api.conf;
sudo supervisorctl reread;
sudo supervisorctl update;
sudo supervisorctl restart jobhunter_api;

# Configure nginx
sudo cp /Users/prathyusha/Documents/job-hunter-api/deploy/nginx_jobhunter_api.conf /etc/nginx/sites-available/jobhunter_api.conf;
sudo rm -rf /etc/nginx/sites-enabled/default;
# sudo rm -rf /etc/nginx/sites-available/jobhunter_api.conf;
sudo rm -rf /etc/nginx/sites-enabled/jobhunter_api.conf;
sudo ln -s /etc/nginx/sites-available/jobhunter_api.conf /etc/nginx/sites-enabled/jobhunter_api.conf;
sudo systemctl restart nginx.service;

echo "DONE! :)"
