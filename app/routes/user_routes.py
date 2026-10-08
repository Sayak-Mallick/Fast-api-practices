from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.security import hash_password
from ..database import get_db
from ..models.users_model import User as UserModel
from ..schemas.users_schema import User, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=UserResponse)
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return {"data": users}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new_user = UserModel(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {new_user}
