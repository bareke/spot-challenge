<div align="center">
  <a style="vertical-align: middle;" class="logo" href="https://www.spotcloud.io/" target="_blank">
    <img src="https://www.spotcloud.io/Logo.png" width="300" alt="Inndico Logo" />
  </a>
  <a style="vertical-align: middle;" class="logo" href="https://fastapi.tiangolo.com/" target="_blank">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="350" alt="FastAPI Logo">
  </a>
</div>

[circleci-image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token=abc123def456
[circleci-url]: https://circleci.com/gh/nestjs/nest

<p align="center">
  FastAPI framework, high performance, easy to learn, fast to code, ready for production.
</p>
<p align="center">
  <a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&amp;branch=master" alt="Test">
  </a>
  <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&amp;label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
  </a>
</p>

## Description

Upload images with FastAPI and Azure

## Environment Variables

*Please make sure you provide the correct credentials before running the project*

```python
# FASTAPI
CONTAINER_APP_NAME="fastapi-dev"
APP_PORT=8000
STORAGE_ACCOUNT="accountexample"
STORAGE_CONTAINER_NAME="test-example"
STORAGE_ACCESS_KEY="Id2qEHNgLKWC5c28=="

# POSTGRESQL
CONTAINER_DATABASE_NAME="postgres-dev"
DATABASE_IMAGE="postgres:12-alpine"
DATABASE_HOST="postgres-dev"
DATABASE_PORT=5432
DATABASE_USER="postgres"
DATABASE_PASSWORD="postgres"
DATABASE_NAME="spot"

# CELERY
CONTAINER_WORKER_NAME="celery-dev"
WORKER_BROKER_URL="redis://redis-dev:6379/0"
WORKER_RESULT_BACKEND="redis://redis-dev:6379/0"

# REDIS
CONTAINER_STORE_NAME="redis-dev"
STORE_IMAGE="redis:7.0-alpine"
STORE_PORT=6379

# FLOWER
CONTAINER_MONITOR_NAME="flower-dev"
MONITOR_PORT=5555
```

## Run project

### Local

```bash
# 1. Create virtual environment
$ python -m venv venv

# 2. Activate virtual environment

# Windows
$ .\venv\Scripts\activate

# Linux
$ source venv/bin/activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Create file .env

# 5. Install database postgresql

# 6. Execute app
$ uvicorn main:app

# 7. Install database redis

# 8. Execute queue
$ celery -A app.settings.worker worker --loglevel=info --logfile=celery.log

# 9. Execute monitor
$ celery --broker=redis://localhost:6379/0 flower --port=5555
```


### Docker compose

```bash
# 1. Create file .env

# 2. Run containers
$ docker compose up -d --build --scale queue=5
```

## Upload images

```bash
# Run the file to send the images
$ python send_images_to_api.py
```
