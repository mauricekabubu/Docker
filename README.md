# 🐳 Docker Fundamentals

A comprehensive repository covering the core concepts of Docker, from creating images to managing containers, persistent storage with volumes, and orchestrating multi-container applications using Docker Compose.

This repository serves as both a learning resource and a practical reference for developers who want to understand how Docker simplifies software development, testing, and deployment.

---

# 📚 Table of Contents

* Introduction
* Why Docker?
* Docker Architecture
* Images
* Containers
* Dockerfile
* Volumes
* Networks
* Docker Compose
* Development Workflow
* Production Workflow
* Common Commands
* Best Practices
* Learning Outcomes

---

# 🚀 Introduction

Docker is a platform that packages applications together with all their dependencies into lightweight, portable units called **containers**.

Instead of worrying about different operating systems, installed libraries, or software versions, developers can run the exact same application in identical environments.

This eliminates the classic problem of:

> "It works on my machine."

---

# ❓ Why Docker?

Docker provides several important benefits:

* Consistent development environments
* Faster onboarding for new developers
* Simplified deployments
* Lightweight virtualization
* Easier scaling
* Better resource utilization
* Reproducible builds

Rather than installing every dependency directly on your computer, Docker isolates everything inside containers.

---

# 🏗 Docker Architecture

At a high level:

```text
Developer
     │
     ▼
 Dockerfile
     │
     ▼
 Docker Image
     │
     ▼
 Docker Container
```

A **Dockerfile** defines how an image should be built.

An **Image** is a reusable blueprint.

A **Container** is a running instance of an image.

---

# 📦 Docker Images

A Docker image is an immutable template containing:

* Application code
* Runtime
* Dependencies
* Libraries
* Environment configuration

Images are built once and can be used repeatedly.

Example:

```bash
docker build -t my-app .
```

List available images:

```bash
docker images
```

Remove an image:

```bash
docker rmi IMAGE_ID
```

---

# 📦 Containers

Containers are running instances of Docker images.

Each container runs in an isolated environment.

Create and run:

```bash
docker run my-app
```

Run in detached mode:

```bash
docker run -d my-app
```

View running containers:

```bash
docker ps
```

View all containers:

```bash
docker ps -a
```

Stop a container:

```bash
docker stop CONTAINER_ID
```

Remove a container:

```bash
docker rm CONTAINER_ID
```

---

# 📝 Dockerfile

A Dockerfile contains instructions for building an image.

Example:

```dockerfile
FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Common instructions:

* FROM
* WORKDIR
* COPY
* ADD
* RUN
* ENV
* EXPOSE
* CMD
* ENTRYPOINT

---

# 💾 Volumes

Containers are temporary.

If a container is removed, any data stored inside it is also removed.

Volumes solve this problem by storing data outside the container.

Example:

```bash
docker volume create my-volume
```

Mount a volume:

```bash
docker run -v my-volume:/app/data my-app
```

Benefits:

* Persistent storage
* Database durability
* Data sharing between containers
* Easier backups

Volumes are especially useful for databases like PostgreSQL, MySQL, and MongoDB.

---

# 🌐 Docker Networks

Containers communicate through Docker networks.

Instead of using IP addresses, containers can communicate using service names.

Example:

```yaml
services:
  backend:
  database:
```

The backend can connect to:

```
database:5432
```

without needing to know the actual IP address.

---

# 🧩 Docker Compose

Docker Compose allows you to define and run multiple containers using a single configuration file.

Instead of manually starting each service individually, Docker Compose manages the entire application stack.

Example services:

* Backend API
* Frontend
* PostgreSQL
* Redis
* Nginx

Example:

```yaml
services:
  backend:
    build: .

  database:
    image: postgres

  redis:
    image: redis
```

Start everything:

```bash
docker compose up
```

Run in background:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

Rebuild:

```bash
docker compose up --build
```

Compose makes local development significantly easier because one command starts the complete application.

---

# 💻 Docker in Development

Docker helps developers by:

* Keeping every developer on the same environment
* Eliminating dependency conflicts
* Making onboarding easier
* Supporting hot reloading with mounted volumes
* Running databases locally without installing them
* Quickly spinning up testing environments

Instead of installing PostgreSQL or Redis directly on your machine, you can simply start them with Docker.

---

# 🚀 Docker in Production

Docker is widely used in production because it enables reliable and repeatable deployments.

Benefits include:

* Identical environments from development to production
* Easier CI/CD pipelines
* Faster deployments
* Easy rollbacks
* Better scalability
* Improved resource efficiency
* Isolation between services

A container built during development is the same container deployed to production.

This greatly reduces deployment-related bugs.

---

# 📂 Typical Project Structure

```
project/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── requirements.txt
├── app.py
└── README.md
```

---

# ⚡ Common Docker Commands

Build an image

```bash
docker build -t my-app .
```

Run a container

```bash
docker run my-app
```

List images

```bash
docker images
```

List running containers

```bash
docker ps
```

Stop a container

```bash
docker stop container_id
```

Remove a container

```bash
docker rm container_id
```

Remove an image

```bash
docker rmi image_id
```

List volumes

```bash
docker volume ls
```

List networks

```bash
docker network ls
```

Start all services

```bash
docker compose up
```

Run in detached mode

```bash
docker compose up -d
```

Stop all services

```bash
docker compose down
```

---

# ✅ Best Practices

* Keep images as small as possible.
* Use official base images whenever possible.
* Store secrets in environment variables instead of images.
* Use `.dockerignore` to reduce build context.
* Use named volumes for persistent data.
* Build once and deploy the same image everywhere.
* Separate development and production configurations when necessary.

---

# 🎯 Learning Outcomes

After completing this repository, you should understand:

* How Docker works internally
* How to build Docker images
* How containers differ from virtual machines
* How to write Dockerfiles
* How volumes provide persistent storage
* How Docker networking enables service communication
* How Docker Compose orchestrates multiple services
* How Docker improves both development and production workflows
* How to package applications for reliable deployment

---

# 📖 References

* Docker Official Documentation: https://docs.docker.com/
* Docker Hub: https://hub.docker.com/

---

## ⭐ Support

If you found this repository helpful, consider giving it a ⭐ to support the project and help others discover it.

Happy containerizing! 🐳
