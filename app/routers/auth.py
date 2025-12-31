"""
Rutas relacionadas con la autenticacion de usuarios en la aplicacion FastAPI.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.user import LoginRequest, TokenResponse
from app.models.user import User
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

"""
dependency para obtener la sesion de la base de datos.
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



"""
endpoint para el login de usuarios.
"""
@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}
