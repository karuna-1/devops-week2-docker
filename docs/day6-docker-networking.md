DAY 6 — DOCKER NETWORKING

1. Docker Networking
Docker networking allows containers to communicate with each other and with the host.

2. Default Docker Networks
- bridge → default network for containers
- host → container uses the host's network
- none → no network connectivity

3. Container IP
Every container on a Docker network can have an internal IP.
Container IPs can change, so avoid hard-coding them.

4. User-defined Network
Create:
docker network create devops-net

Run a container on it:
docker run -d --name web-test --network devops-net nginx

5. Container-to-Container Communication
Containers on the same user-defined network can communicate directly.

Example:
web → api:5000

No -p is required for container-to-container communication.

6. Docker DNS
Docker provides internal DNS on user-defined networks.

Use:
http://api:5000

instead of:
http://172.x.x.x:5000

This is better because container IPs can change.

7. Host Port vs Container Port
-p HOST_PORT:CONTAINER_PORT

Example:
docker run -p 8080:80 nginx

Mac:8080 → Container:80

-p is needed when accessing the container from the host.

8. localhost
On the Mac:
localhost = Mac

Inside a container:
localhost = that same container

Therefore:
web → localhost:5000
usually means the web container itself.

For another container:
web → api:5000

9. Network Connect / Disconnect
Connect:
docker network connect devops-net api

Disconnect:
docker network disconnect devops-net api

A container can be connected to multiple networks.

10. Troubleshooting
If a container cannot communicate:

1. Check containers:
docker ps

2. Check network:
docker network inspect devops-net

3. Check logs:
docker logs <container>

4. Check configuration:
docker inspect <container>

5. Check that the application is listening on the correct container port.

KEY IDEA:
Same Docker network + container name = simple container-to-container communication.