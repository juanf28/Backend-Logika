"""
Importaciones y rutas relacionadas con la gestion de tareas en la aplicacion FastAPI.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut


from app.db.session import SessionLocal
from app.models.task import Task


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    dependencies=[Depends(get_current_user)],
)

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
Endpoints para la gestion de tareas (CRUD).
"""

"""
endpoint para crear una nueva tarea.
"""
@router.post("/", response_model=TaskOut,)
def create_task(
    title: str,
    description: str | None = None,
    user=(get_current_user),
    db: Session = Depends(get_db)
):
    task = Task(
        title=title,
        description=description,
        status="pending"
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


"""
endpoint para listar todas las tareas con paginación.
"""
@router.get("/")
def list_tasks(page: int = Query(1, ge=1), limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
   
    skip = (page - 1) * limit
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return {
        "page": page,
        "limit": limit,
        "tasks": tasks
    }



"""
endpoint para obtener una tarea por su ID.
"""
@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


"""
endpoint para actualizar una tarea existente.
"""
@router.put("/{task_id}",response_model=TaskOut)
def update_task(
    task_id: int,
    title: str | None = None,
    description: str | None = None,
    completed: bool | None = None,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if completed is not None:
        task.completed = completed

    db.commit()
    db.refresh(task)
    return task


"""
endpoint para eliminar una tarea por su ID.
"""
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
