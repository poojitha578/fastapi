from fastapi import FastAPI,APIRouter,Depends,HTTPException
from db_configuration.db_model import User
from sqlalchemy.orm import Session
from db_configuration.db_model import UserBase
from db_configuration.config import SessionLocal
import service.user_service as service

router=APIRouter()

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_user")
async def create_user(user: UserBase, db: Session=Depends(get_db)):
    return await service.create_user(db,user)

@router.get("/read_user")
async def read_user(db: Session=Depends(get_db)):
    return await service.read_user(db)

@router.put("/update_user/{user_id}")
async def update_user(user_id:str, user: UserBase, db: Session=Depends(get_db)):
    return await service.update_user(db, user_id, user)

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id:str,user:UserBase, db:Session=Depends(get_db)):
    return await service.delete_user(db,user_id,user)












