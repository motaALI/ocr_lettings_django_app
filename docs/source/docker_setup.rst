.. _docker_setup:

=============================
Docker Setup for Development
=============================

To facilitate local development and testing, we provide Docker configuration files that streamline the setup process.

Docker Compose Configuration
-----------------------------

The `docker-compose.yml` file defines the services required to run the application:

.. code-block:: yaml

    version: '3'

    services:
      web:
        build:
          context: .
          dockerfile: Dockerfile
        command: gunicorn oc_lettings_site.wsgi --bind 0.0.0.0:8000
        environment:
          - DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
        expose:
          - "8000"
        volumes:
          - .:/app
        ports:
          - "8000:8000"

This configuration sets up a service named `web` that builds the application using the provided `Dockerfile` and runs it using Gunicorn on port 8000.

Building and Running
---------------------

To build and run the application using Docker Compose, execute the following commands:

.. code-block:: shell

    docker-compose build
    docker-compose up

This will build the Docker image and start the containerized application. You can then access the application at http://localhost:8000.

Cleaning Up
------------

To stop the running containers and remove the associated resources, use the following command:

.. code-block:: shell

    docker-compose down

This will stop and remove the containers defined in the `docker-compose.yml` file.

