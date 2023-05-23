import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings.database import Base, engine
from app.settings.environment import settings
from app.settings.routers import routers

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


prefix = "/api"

# Register all routers
[app.include_router(router, prefix=prefix) for router in routers]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
