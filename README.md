Picus CRUD API Service
This repository contains my solution to the backend engineering task. The goal was to implement a simple CRUD API backed by PostgreSQL, containerize the system, and set up a CI/CD pipeline using GitHub Actions.

Application Overview
The application is a RESTful API built using Django and Django REST Framework (DRF). It exposes HTTP endpoints under the /picus path and stores data in a PostgreSQL database.

Implemented Endpoints
The following endpoints were implemented according to the task specification:

GET /picus/list: Returns all items stored in the PostgreSQL table.

POST /picus/put: Saves the given JSON payload into PostgreSQL and returns the generated object ID.

GET /picus/get/{id}: Retrieves the object with the given key from PostgreSQL and returns it in JSON format.

DELETE /picus/{id}: Deletes the object associated with the given key from PostgreSQL.

