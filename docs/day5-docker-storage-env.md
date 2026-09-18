# Day 5 — Docker Volumes, Bind Mounts & Environment Variables

## 1. Container Filesystem

Data stored directly inside a container is temporary.

If the container is deleted, its data is deleted.

```text
Container → deleted
Container data → deleted
```

---

## 2. Docker Volumes

A Docker volume provides persistent storage managed by Docker.

### Create a volume

```bash
docker volume create my-data
docker volume ls
```

### Mount a volume

```bash
docker run -it --name volume-test -v my-data:/data ubuntu
```

Inside the container:

```bash
echo "This data should survive" > /data/message.txt
cat /data/message.txt
```

Delete the container:

```bash
docker rm volume-test
```

The volume still exists:

```bash
docker volume ls
```

Attach the volume to a new container:

```bash
docker run --rm -it -v my-data:/data ubuntu
```

Check the data:

```bash
cat /data/message.txt
```

The data is still available.

### Key idea

**Container = temporary**

**Volume = persistent**

---

## 3. Bind Mounts

A bind mount connects a specific folder or file on the host machine to a folder inside the container.

Example:

```bash
docker run --rm -it -v "$(pwd)":/data ubuntu
```

Here:

```text
$(pwd) → current folder on the Mac
/data  → folder inside the container
```

Changes made on the Mac are visible inside the container.

### Common use

Bind mounts are useful during development because source code can be edited on the host while the container accesses the same files.

---

## 4. Volume vs Bind Mount

| Volume | Bind Mount |
|---|---|
| Managed by Docker | Uses a specific host path |
| Good for persistent data | Good for development |
| `my-data:/data` | `$(pwd):/data` |

### Easy memory trick

**Volume = Docker manages the storage**

**Bind mount = I choose the host folder**

---

## 5. Environment Variables

Environment variables separate application configuration from application code.

Examples:

```text
APP_ENV=development
PORT=5000
DATABASE_URL=...
```

### Pass an environment variable

```bash
docker run --rm -e APP_ENV=development ubuntu env
```

For production:

```bash
docker run --rm -e APP_ENV=production ubuntu env
```

The same Docker image can use different configurations without rebuilding the image.

```text
Same image
├── development
├── testing
└── production
```

---

## 6. Environment Variables in Flask

Python uses the `os` module to read environment variables.

```python
import os

environment = os.getenv("APP_ENV", "development")
```

Example:

```python
@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "development")
    return f"Hello from Docker! Environment: {environment}"
```

`"development"` is the default value if `APP_ENV` is not provided.

---

## 7. `.env` File

A `.env` file can store environment variables.

Example:

```text
APP_ENV=development
PORT=5000
```

Load the variables using:

```bash
docker run --env-file .env ...
```

### Security

Do not commit secrets to GitHub.

Examples:

```text
DATABASE_PASSWORD=...
API_KEY=...
SECRET_KEY=...
```

Add `.env` to `.gitignore`:

```text
.env
```

---

## 8. `.gitignore` vs `.dockerignore`

### `.gitignore`

Controls what Git ignores.

Example:

```text
.env
```

### `.dockerignore`

Controls what is excluded from the Docker build context.

Example:

```text
.git
.env
```

---

## 9. Build vs Runtime Configuration

### Code changes

Usually require rebuilding the image:

```text
Change app.py
    ↓
docker build
    ↓
New image
```

### Configuration changes

Can usually be supplied at runtime:

```text
Same image
    ↓
APP_ENV=production
```

No image rebuild is required just because the runtime configuration changes.

---

## 10. Day 5 Commands

```bash
# Volumes
docker volume create my-data
docker volume ls
docker run -v my-data:/data ...

# Bind mount
docker run -v "$(pwd)":/data ...

# Environment variable
docker run -e KEY=value ...

# .env file
docker run --env-file .env ...
```

---