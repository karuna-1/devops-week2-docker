# Day 9 – Dockerized Web Application

## Objective
Build a simple Web + API application using Docker, Docker Networking, Environment Variables, and Docker Compose.

## Architecture

Browser
   ↓
localhost:5002
   ↓
Web Container
   ↓
http://api:5001
   ↓
API Container

## API
- Flask API runs on port `5001`
- Endpoint: `GET /api`
- Response: `Hello from API v2`
- API was built into Docker images `v1` and `v2`

## Web
- Flask Web app runs on port `5002`
- Web sends requests to the API
- API URL is stored in an environment variable

## Docker Networking
Created a custom network:

    docker network create day9-network

Containers on the same Docker network can communicate using names instead of IP addresses.

Example:

    http://api:5001

Docker DNS resolves `api` to the API container.

## Environment Variables
`.env`:

    API_URL=http://api:5001

The `.env` file is excluded using `.gitignore`.

## Docker Compose
Used `compose.yaml` with two services:

- `api`
- `web`

The Web service publishes:

    5002:5002

The API is internal and does not publish port `5001` to the host.

Started the application:

    docker compose up --build

Checked services:

    docker compose ps

## Testing

    curl http://localhost:5002

Response:

    <h1>Web App</h1><p>Hello from API v2</p>

This confirmed:

    Browser → Web → API

## Logs

Checked logs:

    docker compose logs
    docker compose logs web
    docker compose logs api

HTTP `200` in the logs means the request was successful.

## Troubleshooting
A port conflict occurred on port `5000`, so the application used:

- API → `5001`
- Web → `5002`

A container-name conflict was fixed by removing the old containers.

Troubleshooting order:

    docker compose ps
    docker compose logs web
    docker compose logs api
    docker network inspect <network-name>

## Stopping the Application

    docker compose down

This removed:

- Web container
- API container
- Docker network

The Docker images remained.

## Key Learnings
- Docker Compose manages multiple services.
- Containers communicate through Docker networks.
- Docker DNS allows service-name communication.
- Internal services do not need published host ports.
- Environment variables separate configuration from code.
- `docker compose logs` helps troubleshoot applications.
- `docker compose down` removes containers and networks, but not images.
- Troubleshoot layer by layer.