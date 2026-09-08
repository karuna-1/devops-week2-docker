# Day 2 — Docker CLI & Container Management

Today I learned how to manage Docker containers from the terminal.

## 🐳 Container Lifecycle

A container can be:

**Stopped → Running → Stopped**

* `docker start` → starts an existing stopped container
* `docker stop` → stops a running container
* `docker restart` → stops and starts a container again
* `docker rm` → deletes the container

> `docker rm` does **not** delete the image.

## 🔍 Useful Docker Commands

```bash
docker ps
```

Shows currently running containers.

```bash
docker ps -a
```

Shows all containers, including stopped ones.

```bash
docker logs <container>
```

Shows the application's/container's output. Very useful for troubleshooting.

```bash
docker exec <container> <command>
```

Runs a command inside a running container.

For an interactive shell:

```bash
docker exec -it <container> /bin/bash
```

```bash
docker inspect <container>
```

Shows detailed information about a container such as its image, state, networking, IP address and port mappings.

## 🌐 Nginx Practice

I used an Nginx container to practice these commands.

My container had:

```text
Host:     localhost:8080
              ↓
Docker:   8080 → 80
              ↓
Container: port 80
              ↓
Nginx
```

I also used `docker inspect` to find the container IP and confirm the port mapping.

## 🛠️ Troubleshooting

If a container is running but the application isn't working, two good first checks are:

```bash
docker logs <container>
docker inspect <container>
```

**Logs** → What is the application saying?

**Inspect** → Is the container configured correctly?

## 💡 What I understood today

An image is the blueprint, while a container is an instance created from that image. Multiple containers can use the same image.

Today I actually started, stopped, restarted, inspected, entered and removed Docker containers instead of just learning the commands theoretically.
