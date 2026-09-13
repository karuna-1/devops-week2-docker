# Day 4 — Docker Hub

## Docker Hub
Docker Hub is a container registry used to store and distribute Docker images.

## Registry vs Docker Hub
- Registry = service that stores/distributes container images.
- Docker Hub = a popular container registry.

## Image Tags
Docker Hub images use:

username/repository:tag

Example:
karuna2002/my-first-docker-app:v2

## Docker Commands

docker login
- Authenticates with Docker Hub.

docker tag
- Gives an existing image another tag/name.

docker push
- Uploads an image to Docker Hub.

docker pull
- Downloads an image from Docker Hub.

docker run
- Creates and starts a container from an image.

## Docker Hub Workflow

Dockerfile
↓ docker build
Local Image
↓ docker tag
username/repository:v2
↓ docker push
Docker Hub
↓ docker pull
Production Server
↓ docker run
Container

## Public vs Private
- Public repository → others can pull the image.
- Private repository → access is restricted.

## Hands-on Achievement
- Created a Dockerized Flask application.
- Tagged it as karuna2002/my-first-docker-app:v2.
- Pushed it to Docker Hub.
- Removed the local copy.
- Pulled the image back from Docker Hub.
- Ran the pulled image successfully.
- Accessed the application through localhost:8082.

## Key Learning
Docker images can be packaged once, stored in a registry, and pulled onto other machines for consistent deployment.