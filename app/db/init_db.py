from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password

"""
Crear un usuario inicial en la base de datos si no existe."""
def create_initial_user(db: Session):
    user = db.query(User).filter(User.username == "admin").first()
    if not user:
        user = User(
            username="admin",
            hashed_password=hash_password("admin123")
        )
        db.add(user)
        db.commit()
