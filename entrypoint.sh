#!/bin/sh

# Creating docker network
echo "Creating custom elx-network for docker internal communications"
sudo docker network create app-network

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Creating database migrations
echo "collecting database migrations"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate --database=default

# Check if PROD environment variable is set to true
if [ "$PROD" = "true" ]; then
    echo "Starting Gunicorn"
    gunicorn \
        --workers=4 \
        --threads=6 \
        --worker-class=gthread \
        --preload \
        --bind :8000 \
        --log-level=info \
        --error-logfile - \
        --access-logfile - \
        --capture-output \
        elx_chatbot_admin_backend.wsgi:application
else
    echo "Starting development server"
    python manage.py runserver 0.0.0.0:8000

fi