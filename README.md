Picus CRUD API Service
This repository contains my solution to the backend engineering task. The goal was to implement a simple CRUD API backed by PostgreSQL, containerize the system, and set up a CI/CD pipeline using GitHub Actions.

Application Overview
The application is a RESTful API built using Django and Django REST Framework (DRF). It exposes HTTP endpoints under the /picus path and stores data in a PostgreSQL database.

1. Implemented Endpoints
   
The following endpoints were implemented according to the task specification:

GET /picus/list: Returns all items stored in the PostgreSQL table.

POST /picus/put: Saves the given JSON payload into PostgreSQL and returns the generated object ID.

GET /picus/get/{id}: Retrieves the object with the given key from PostgreSQL and returns it in JSON format.

DELETE /picus/{id}: Deletes the object associated with the given key from PostgreSQL.

2. Docker Image
   
The application is containerized using a Dockerfile based on python:3.13.3-slim.
All dependencies are installed from requirements.txt, the application runs inside the /app directory, and the Django server is started via a custom entrypoint script (django.sh). The container exposes port 8000.


3. Docker Compose Setup
   
The project includes a docker-compose.yml file that runs the following services:
Django application
Runs internally and listens on port 8000. It is not exposed externally and is only accessible by Nginx.
PostgreSQL
Runs as a separate container with data persisted using Docker volumes. The database is only accessible by the application container.
Nginx (Reverse Proxy)
Nginx is the only externally accessible service. It listens on port 80 and forwards all /picus/* requests to the Django application container.
The services communicate over Docker’s internal network, ensuring that only Nginx is exposed to the outside world.

Service Startup Order:

Although depends_on is used in docker-compose.yml to control container startup order, it does not guarantee database readiness.
To handle this, the application includes error handling for database connection issues and returns a 503 Service Unavailable response when PostgreSQL is not yet available. This allows the application to start reliably in containerized environments.

Nginx Reverse Proxy:

Nginx is configured as a reverse proxy to forward all requests under /picus/ to the Django application running on port 8000.
The routing is defined in the Nginx configuration file and ensures that the application container is only accessible through Nginx


