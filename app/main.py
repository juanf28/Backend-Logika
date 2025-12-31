
"""
Importaciones y configuracion principal de la aplicacion FastAPI.

"""
from fastapi import FastAPI

from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models import user, task
from app.db.init_db import create_initial_user
from app.routers import auth
from app.routers import task

app = FastAPI(
    title="Logika Backend Test",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    create_initial_user(db)
    db.close()

@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(auth.router)
app.include_router(task.router)    


