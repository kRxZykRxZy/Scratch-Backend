# 🐳 Python Auto Dependency Installer (Dockerized)

This project scans Python files inside the `src/` folder to:

- Automatically detect and install third-party dependencies.
- Serve or run code inside a Docker container.
- Treat `src/` as a clean Python module with `__init__.py` support.

Useful for rapid prototyping, API services, or modular apps.

## 🚀 Getting Started

### 🔧 1. Build the Docker Image

```bash
docker build -t python-module-installer .

docker run --rm python-module-installer
```
If this doesnt work use:
```py
python -m resources.src.main
```
<!--
## 🔒 Internal API Reference

Use this section to document endpoints for internal or backend APIs.

### 🟢 GET /status

Returns system status.

```bash
curl -X GET http://localhost:8000/status
