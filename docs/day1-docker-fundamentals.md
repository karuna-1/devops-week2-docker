# Day 1 — Docker Fundamentals

**Week:** Month 1 — Week 2
**Topic:** Docker Fundamentals
**Date:** September 7, 2026

---

## 1. What is Docker?

Docker is a platform that allows us to **package and run applications in containers**.

One problem Docker helps solve is the difference between environments.

For example:

```text
My Machine
Python 3.11
    ↓
Application works ✅

Another Machine
Python 3.9
    ↓
Application might fail ❌
```

An application may depend on:

* A specific programming language version
* Specific libraries
* Specific dependencies
* Configuration
* System requirements

Docker helps create a more consistent environment for running the application.

### Simple definition

> Docker is a platform for packaging and running applications in containers.

---

## 2. Why is Docker Useful in DevOps?

DevOps involves moving applications through different environments:

```text
Development
     ↓
Testing
     ↓
Staging
     ↓
Production
```

We want the application to behave consistently across these environments.

Docker helps package the application and its required environment so that it can be run more predictably on different machines.

---

## 3. What is a Container?

A **container** is a lightweight, isolated environment that packages an application with what it needs to run.

```text
┌─────────────────────────┐
│       Container         │
│                         │
│  Application            │
│  Dependencies           │
│  Configuration          │
│                         │
└─────────────────────────┘
```

### Simple definition

> A container is a lightweight, isolated unit that packages an application with what it needs to run.

### Important clarification

A container is primarily about **running** an application and its dependencies, not necessarily everything required to build the application.

---

## 4. What is a Docker Image?

A Docker **image** is a blueprint or template used to create containers.

```text
Image
  ↓
docker run
  ↓
Container
```

For example:

```text
nginx IMAGE
     ↓
nginx CONTAINER
```

### Simple definition

> An image is a blueprint/template containing the files, dependencies, and instructions needed to create and run a container.

---

## 5. Image vs Container

The image and container are different things.

```text
IMAGE
  ↓
Template / Blueprint
  ↓
CONTAINER
  ↓
Instance created from the image
```

One image can be used to create multiple containers.

```text
              nginx IMAGE
             /     |     \
            ↓      ↓      ↓
       Container Container Container
```

### Key point

> **Image ≠ Container**

An image is the template.

A container is an instance created from that image.

---

## 6. Containers vs Virtual Machines

### Virtual Machine

A simplified VM architecture:

```text
Physical Computer
       ↓
    Host OS
       ↓
   Hypervisor
       ↓
    Guest OS
       ↓
   Application
```

A VM typically includes its own guest operating system.

### Container

A simplified container architecture:

```text
Physical Computer
       ↓
    Host OS
       ↓
 Docker Engine
       ↓
   Container
       ↓
  Application
```

Containers share the host operating system's **kernel** instead of each requiring a complete guest operating system.

### Why are containers lightweight?

Because containers generally don't need a complete guest OS for each application.

### Interview answer

> Containers share the host OS kernel, whereas virtual machines typically have their own guest operating system.

---

# 7. Docker CLI

The **Docker CLI** is the command-line interface that we use to communicate with Docker.

Examples:

```bash
docker run
docker ps
docker images
```

When I type:

```bash
docker run nginx
```

I am using the Docker CLI.

---

# 8. Docker Daemon

The **Docker daemon** is a background service that performs Docker operations.

It manages things such as:

* Containers
* Images
* Networks
* Volumes

The basic relationship is:

```text
User
  ↓
Docker CLI
  ↓
Docker Daemon
  ↓
Docker performs the requested operation
```

When I ran:

```bash
docker run hello-world
```

the Docker client contacted the Docker daemon.

The daemon then handled the Docker operations.

---

# 9. Docker Engine

Docker Engine is the core Docker technology that allows us to build and run containers.

For now, the important mental model is:

```text
Docker CLI
     ↓
Docker Engine / Daemon
     ↓
Containers / Images / Networks / Volumes
```

---

# 10. Docker Hub

**Docker Hub** is a registry where Docker images can be stored and shared.

When I ran:

```bash
docker run hello-world
```

Docker was able to obtain the `hello-world` image from Docker Hub.

The simplified flow was:

```text
Docker CLI
    ↓
Docker Daemon
    ↓
Docker Hub
    ↓
hello-world Image
    ↓
Container
```

---

# 11. My First Docker Command

I verified that Docker was installed using:

```bash
docker --version
```

Output:

```text
Docker version 29.4.0
```

This confirmed that the Docker CLI was installed.

---

# 12. My First Docker Container

I ran:

```bash
docker run hello-world
```

Docker performed these steps:

```text
Docker CLI
    ↓
Docker Daemon
    ↓
Pull hello-world image
    ↓
Create container
    ↓
Run container
    ↓
Print output
    ↓
Container exits
```

The `hello-world` container successfully completed its task.

---

# 13. Why Did hello-world Stop?

The container's lifecycle is closely connected to its main process.

The `hello-world` container:

```text
Start
  ↓
Print message
  ↓
Process finishes
  ↓
Container stops
```

The container did not crash.

It simply completed its task.

This resulted in:

```text
Exited (0)
```

---

# 14. Understanding Exit Codes

An exit code of:

```text
0
```

generally means the process completed successfully.

Example:

```text
Exited (0)
```

means the process finished successfully.

My `monitoring-app` container showed:

```text
Exited (255)
```

This indicates that the process did not finish successfully and would require troubleshooting.

---

# 15. `docker ps`

The command:

```bash
docker ps
```

shows **currently running Docker containers**.

Example:

```text
CONTAINER ID
IMAGE
COMMAND
CREATED
STATUS
PORTS
NAMES
```

It does not show stopped containers.

---

# 16. `docker ps -a`

The command:

```bash
docker ps -a
```

shows **all containers**, including:

* Running containers
* Stopped containers

For example, my `hello-world` container appeared here:

```text
hello-world
Exited (0)
```

It did not appear in:

```bash
docker ps
```

because it was no longer running.

---

# 17. `docker images`

The command:

```bash
docker images
```

shows Docker images available locally on the machine.

My machine currently has images including:

```text
aegis_v1:latest
firstjava-app:latest
hello-world:latest
monitoring-app:latest
my-first-image:latest
nginx:latest
ubuntu:latest
```

---

# 18. Image Names and Tags

An image can have a name and tag.

Example:

```text
hello-world:latest
     ↑          ↑
    name       tag
```

`latest` is a tag.

Image tags will be explored more when learning Docker image building and Docker Hub.

---

# 19. What is Nginx?

**Nginx** is a web server that can also act as a reverse proxy.

Nginx can:

* Receive HTTP requests
* Serve website files
* Forward requests to backend applications

A simple flow:

```text
Browser
   ↓
Nginx
   ↓
HTTP Response
   ↓
Browser
```

Nginx commonly listens for HTTP traffic on:

```text
Port 80
```

---

# 20. Running Nginx in Docker

I ran:

```bash
docker run nginx
```

This created a container from the existing `nginx` image.

The container stayed running because Nginx is a web server whose main process continues listening for incoming requests.

```text
Nginx
  ↓
Listen for requests
  ↓
Keep running
  ↓
Container stays running
```

---

# 21. Docker Ports

A port can be thought of as a numbered doorway through which network traffic can enter or leave a system.

Some common ports:

```text
22  → SSH
53  → DNS
80  → HTTP
443 → HTTPS
```

Nginx commonly listens on:

```text
80
```

inside its container.

---

# 22. Container Port vs Host Port

This is one of the most important Docker concepts.

When we run:

```bash
docker run -p 8080:80 nginx
```

the format is:

```text
-p HOST_PORT:CONTAINER_PORT
```

Therefore:

```text
8080 → Host port (Mac)
80   → Container port
```

The traffic flow is:

```text
Browser
   ↓
localhost:8080
   ↓
Mac port 8080
   ↓
Docker port mapping
   ↓
Nginx container port 80
   ↓
Nginx
   ↓
HTTP response
```

### Important

Docker does **not** change Nginx's internal port from 80 to 8080.

Nginx still listens on:

```text
80
```

Docker simply maps the host port to the container port.

---

# 23. My Nginx Port Mapping Experiment

I ran:

```bash
docker run -p 8080:80 nginx
```

Then I opened:

```text
http://localhost:8080
```

in my browser.

I successfully received:

```text
Welcome to nginx!
```

This demonstrated:

```text
localhost:8080
       ↓
Host port 8080
       ↓
Docker port mapping
       ↓
Container port 80
       ↓
Nginx
       ↓
Welcome page
```

---

# 24. Important Docker Commands Learned

| Command                 | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| `docker --version`      | Check Docker version                       |
| `docker run IMAGE`      | Create and start a container from an image |
| `docker ps`             | Show running containers                    |
| `docker ps -a`          | Show all containers                        |
| `docker images`         | Show local Docker images                   |
| `docker stop CONTAINER` | Stop a running container                   |

Only the commands actually practiced today are being documented. More Docker commands will be added as they are learned.

---

# 25. Key Mental Model

The most important Docker relationship from Day 1:

```text
                 Docker Hub
                     ↓
                   IMAGE
                     ↓
                docker run
                     ↓
                 CONTAINER
                     ↓
              Main Process
                ↙       ↘
            Running     Exits
               ↓          ↓
          Container    Container
           running      stopped
```

---

# 26. Docker Networking Mental Model

For the Nginx experiment:

```text
Browser
   ↓
localhost:8080
   ↓
Host/Mac :8080
   ↓
Docker port mapping
   ↓
Nginx Container :80
   ↓
Nginx
   ↓
HTTP Response
```

---

# 27. Day 1 Practical Work

Today I successfully:

* [x] Verified Docker installation
* [x] Ran `hello-world`
* [x] Observed Docker CLI → daemon interaction
* [x] Observed an image being pulled
* [x] Created a container
* [x] Used `docker ps`
* [x] Used `docker ps -a`
* [x] Used `docker images`
* [x] Ran Nginx
* [x] Published a container port
* [x] Accessed Nginx through `localhost:8080`
* [x] Understood host port vs container port

---

# 28. Interview Questions I Can Currently Answer

### Q1. What is Docker?

Docker is a platform for packaging and running applications in containers.

### Q2. What is a container?

A container is a lightweight, isolated unit that packages an application with what it needs to run.

### Q3. What is an image?

An image is a blueprint/template used to create containers.

### Q4. What is the difference between an image and a container?

An image is a template, while a container is an instance created from that image.

### Q5. Why are containers lightweight compared with VMs?

Containers share the host OS kernel instead of each requiring a complete guest OS.

### Q6. What does `docker ps` show?

It shows currently running Docker containers.

### Q7. What does `docker ps -a` show?

It shows all Docker containers, including stopped containers.

### Q8. What does `Exited (0)` mean?

It generally means the container's main process completed successfully.

### Q9. What does `-p 8080:80` mean?

It maps port 8080 on the host to port 80 inside the container.

### Q10. Why did the Nginx container keep running while `hello-world` stopped?

Nginx's main process continues running and listening for requests, while `hello-world` finishes its task and exits.

---

# 29. What I Need to Learn Next

Next topics will be introduced gradually:

* More Docker container commands
* `docker start`
* `docker stop`
* `docker restart`
* `docker rm`
* `docker logs`
* `docker exec`
* `docker inspect`
* Docker images in more depth
* Dockerfiles
* Image layers
* Building my own image
* Docker networking
* Volumes
* Environment variables
* Docker Compose

I will learn each concept through hands-on practice rather than memorizing commands.

---

# Day 1 Summary

> **Docker allows applications to be packaged and run in containers. Images act as templates, containers are instances created from images, and the Docker daemon manages Docker operations. I also learned how Docker can publish a container's port to the host and successfully accessed an Nginx container through `localhost:8080`.**
