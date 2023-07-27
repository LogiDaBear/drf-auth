
# Lab - Class 33 
## Project: drf-auth
## Author: Logan Reese

# Feature Tasks and Requirements
## Features - Django
- Add JWT Authentication to your API.
- Install needed libraries in project configuration and/or site settings.
- Keep any pre-existing authentication so DRF Browsable API still usable.
- Install needed libraries in project configuration and/or site settings.
## Features - Docker
- Switch to using Gunicorn instead of Django’s built in development server.
- mind the number of workers to avoid sluggishness
- Warning You will run into styling issues when you switch over to Gunicorn.
- On Django side you’ll need to properly handle static files using Whitenoise
- Storage Options
- Your choice of SQLite or PostgreSQL
- Adjust docker-compose.yml so that data is persisted in a volume outside of container.
- These steps are different depending on whether SQLite or PostgreSQL is being used.

NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
create Dockerfile based off python:3.10-slim
create docker-compose.yml to run Django app as a web service.
enter docker compose up --build to start your site.
add postgres as a service. Note: It is not required to include a volume so that data can persist when container is shut down.
Go to browsable api and confirm site properly restricts users based on their permissions.
## Contributions
TAs and class 401d22

## Setup
No env variables -> used Docker
## How to initialize/run your application
python manage.py runserver
docker compose up --build
runs at http://localhost:8000/api/v1/uaps
## Libraries / Requirements

- asgiref==3.7.2
- Django==4.2.3
- django-environ==0.10.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.2.2
- gunicorn==21.2.0
- packaging==23.1
- psycopg2-binary==2.9.6
- PyJWT==2.8.0
- pytz==2023.3
- sqlparse==0.4.4
- typing_extensions==4.7.1
- whitenoise==6.5.0

## Tests
Built-in Django testing

python manage.py test