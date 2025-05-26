from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.events import router as events_router
from api.db.sessions import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database before app starts
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(events_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "Worlders"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}