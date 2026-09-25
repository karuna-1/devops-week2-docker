# Day 8 – Networking Fundamentals

## Networking Basics

- **IP Address** identifies a device on a network.
- **IPv4** example: `192.168.1.10`
- **localhost / 127.0.0.1** refers to the current machine or environment.
- **Port** identifies a service running on a machine.

Common ports:

| Port | Service |
|------|---------|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |

## TCP and UDP

- **TCP** – reliable and ordered communication.
- **UDP** – connectionless communication with lower overhead.

## DNS

DNS converts domain names into IP addresses.

```text
google.com → IP address
```

Docker also uses internal DNS, allowing containers to communicate using service names.

```text
web → api
```

## Networking Commands

```bash
nslookup google.com
ping -c 4 google.com
traceroute google.com
curl https://example.com
lsof -i :8080
netstat -an | grep LISTEN
```

## SSH and SCP

SSH is used to securely access a remote server.

```bash
ssh username@server-ip
```

SCP is used to securely copy files.

```bash
scp app.py username@server-ip:/home/username/
```

Never expose or commit private SSH keys.

## HTTP and HTTPS

HTTP follows a request-response model.

```text
Client → HTTP Request → Server
Client ← HTTP Response ← Server
```

Common HTTP methods:

- `GET` – retrieve data
- `POST` – create/send data
- `PUT` – update data
- `DELETE` – delete data

Status codes:

- `2xx` – Success
- `3xx` – Redirect
- `4xx` – Client/request error
- `5xx` – Server error

HTTPS uses TLS to provide encrypted and secure communication.

## Docker Networking

Host to container:

```text
localhost:8080 → container:5000
```

Container to container:

```text
http://web:5000
```

Containers on the same Docker network can communicate using service names instead of hard-coded IP addresses.

## Troubleshooting

```bash
docker ps
docker ps -a
docker logs <container>
docker network inspect <network>
lsof -i :8080
curl http://localhost:8080
```

### Key Takeaway

Networking knowledge helps troubleshoot connectivity between users, hosts, Docker containers, and services.