Day 7 – Docker Compose

Docker Compose:
Docker Compose is used to define and manage multiple containers/services for an application using a compose.yaml file.

Service:
A service represents a containerized application/component managed by Compose.
Example: web service and api service.

compose.yaml:
Defines services, builds, ports, networks, volumes, and environment variables.

Basic commands:
docker compose up
docker compose up -d
docker compose down
docker compose ps
docker compose logs
docker compose logs web
docker compose logs api

Port mapping:
"8080:5000"
8080 = host/Mac port
5000 = container port

Docker Compose networking:
Compose automatically creates a network for services.
Services on the same network can communicate using service names.

Example:
Web → http://api

localhost means the current container.
Service name such as api means another container/service.

Volumes:
Volumes store data separately from the container filesystem.
Data can survive when the container is deleted.

Environment variables:
Environment variables keep configuration separate from application code.

Example:
APP_ENV=development

Compose can use:
environment:
  APP_ENV: ${APP_ENV}

.env:
Stores environment variable values locally.
Do not commit sensitive information.

depends_on:
Controls service startup order.

Example:
web:
  depends_on:
    - api

This means Compose starts api before web.
It does not guarantee that api is fully ready.

Troubleshooting:
1. Check service status:
docker compose ps

2. Check logs:
docker compose logs web
docker compose logs api

Basic troubleshooting flow:
Something doesn't work
→ docker compose ps
→ identify affected service
→ docker compose logs <service>

Mini-project:
Web container → Flask :5000
API container → Nginx :80

Browser:
localhost:8080 → Web container

Web:
http://api → API container

Key learning:
Docker Compose makes it easier to define, start, connect, configure, and troubleshoot multiple containers as one application.