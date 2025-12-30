from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema para crear una tarea
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"  # default "pending"

# Schema para actualizar una tarea
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

# Schema de salida (respuesta)
class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        orm_mode = True  # Muy importante para que SQLAlchemy funcione con Pydantic
