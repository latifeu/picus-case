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

4. CI/CD Pipeline (GitHub Actions)
   
Testing:

The project includes unit tests focused on the User model to verify correct ORM behavior.
The implemented tests cover:
Creating a user and verifying persisted fields
Validating field constraints such as name length
Basic email format validation
Creating and retrieving multiple records
Retrieving a user by primary key
Updating existing records
Deleting records and verifying removal
Filtering records by name and email
All tests are implemented using Django’s TestCase.
Test Database Configuration
During test execution, the application automatically switches from PostgreSQL to an in-memory SQLite database.
This keeps tests fast, isolated, and independent from external services, making them suitable for automated CI pipelines.
PostgreSQL is used only in runtime environments, not during unit testing.

Integration tests were initially considered. However, running them in the CI environment would require building the Docker image, starting the full docker-compose stack, waiting for PostgreSQL to become available, and applying database migrations before executing the tests.
An attempt was made to address database readiness using fixed delays (e.g., sleep). However, this approach proved unreliable, as the required wait time could not be determined consistently across environments. To keep the CI pipeline simple, stable, and fast, integration tests were intentionally not included.

Docker Image Build and Push to Docker Hub:

As part of the GitHub Actions pipeline, the Docker image is built using the provided Dockerfile after all tests pass successfully. The image is then tagged and pushed to Docker Hub.


The application reads its configuration from environment variables, particularly for database connectivity.
Database name, user, password, host, and port are injected via Docker Compose and consumed in Django using os.environ.
This allows the same Docker image to run in different environments without code changes.

PostgreSQL data is persisted by using a Docker volume (pgdata) connected to PostgreSQL’s data directory (/var/lib/postgresql/data), so the data is not lost when containers stop or restart.

Application Startup Behavior:

The application is designed to start even if the database is not immediately available.
If the database connection is not ready during startup, the API endpoints intentionally return a custom “database connection not ready” error.
Once the database becomes available and migrations are applied, the application continues to run normally and all endpoints start responding correctly.
If a previously existing database volume is present, the application also starts and works without any issues.

Running the Application


To run the application using Docker, follow these steps:
Pull the Docker image
docker pull lustun/picus-project:last-version
Clone the repository
git clone <your-github-repo-url>
cd <repo-directory>
Start the application using Docker Compose
docker-compose -f docker-compose-production.yml up -d
This command starts Nginx, the Django application, and PostgreSQL containers.
Run database migrations
After waiting a short time for the database container to initialize, run:
docker exec djangoapp python manage.py migrate
Once migrations are completed, the application is fully ready and can be accessed through Nginx.



