import os

from dotenv import load_dotenv

load_dotenv()

settings = {
    "app": {
        "PORT": os.getenv("APP_PORT"),
    },
}
