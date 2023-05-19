import os

from dotenv import load_dotenv

load_dotenv()

settings = {
    "app": {
        "CONTAINER_APP": os.getenv("CONTAINER_APP_NAME"),
        "PORT": os.getenv("APP_PORT"),
    },
}
