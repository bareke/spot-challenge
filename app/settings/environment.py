from os import getenv

from dotenv import load_dotenv

load_dotenv()

settings = {
    "app": {
        "container_app": getenv("CONTAINER_APP_NAME"),
        "port": getenv("APP_PORT"),
    },
    "database": {
        "container_database": getenv("CONTAINER_DATABASE_NAME"),
        "host": getenv("DATABASE_HOST"),
        "port": getenv("DATABASE_PORT"),
        "user": getenv("DATABASE_USER"),
        "password": getenv("DATABASE_PASSWORD"),
        "name": getenv("DATABASE_NAME"),
    },
    "storage": {
        "container_name": getenv("STORAGE_CONTAINER_NAME"),
        "connection_string": f"DefaultEndpointsProtocol=https;AccountName={getenv('STORAGE_ACCOUNT')};AccountKey={getenv('STORAGE_ACCESS_KEY')};EndpointSuffix=core.windows.net",
    },
    "celery": {
        "broker_url": getenv("WORKER_BROKER_URL"),
        "result_backend": getenv("WORKER_RESULT_BACKEND"),
        "imports": {
            "app.image.tasks",
        },
    },
}
