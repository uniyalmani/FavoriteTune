# FavoriteTune Django Project

## Overview

FavoriteTune is a Django project that allows users to discover and save their favorite tunes. The project is containerized using Docker and managed with Docker Compose.

## Prerequisites

Make sure you have the following installed on your machine:

- Docker: [Get Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/uniyalmani/FavoriteTune.git
    ```

2. Navigate to the project directory:

    ```bash
    cd FavoriteTune
    ```


## Using Docker Compose

Alternatively, you can use Docker Compose to manage the services:

1. Build and start the services:

    ```bash
    docker-compose up -d
    ```

2. Open your browser and visit [http://localhost:8000](http://localhost:8000) to access the FavoriteTune app.

3. To stop the services:

    ```bash
    docker-compose down
    ```

## Notes

- Make sure to update the Django settings, database configurations, and other environment-specific configurations in your Django project.
- Customize the Dockerfile and docker-compose.yml files according to your project's needs.

## GitHub Repository

Visit the [FavoriteTune GitHub Repository](https://github.com/uniyalmani/FavoriteTune) for more details.

