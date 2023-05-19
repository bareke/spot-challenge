import uvicorn
from fastapi import FastAPI

from app.settings.environment import settings
from app.settings.routers import routers

app = FastAPI()

prefix = "/api"

# Register all routers
[app.include_router(router, prefix=prefix) for router in routers]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
