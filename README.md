# Dockerized Web Application

A simple multi-container application built using Docker, Flask, Docker Networking, and Docker Compose.

## Architecture

Browser → Web Container → API Container

## Services

- **Web:** Flask application running on port 5002.
- **API:** Flask API running on port 5001.
- **Docker Network:** Allows Web and API containers to communicate.
- **Docker Compose:** Manages both services.

## Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- Docker Networking

## Run the Project

Clone the repository:

    git clone <your-repository-url>

Navigate into the project:

    cd devops-week2-docker

Start the application:

    docker compose up --build -d

Open in your browser:

    http://localhost:5002

## Useful Commands

    docker compose ps
    docker compose logs
    docker compose restart api
    docker compose down

## Key Learnings

- Building Docker images and containers.
- Container-to-container communication.
- Docker DNS and networking.
- Environment variables.
- Docker Compose.
- Health checks.
- CPU and memory limits.
- Container troubleshooting.