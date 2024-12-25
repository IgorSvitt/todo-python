from fastapi import FastAPI
from routers import todo
from db import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ToDo API",
    description="TODO Docks",
    docs_url="/docs",
    redoc_url=None,
)

app.include_router(todo.router)
