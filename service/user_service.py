from db_configuration.db_model import User,UserBase
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException


#Function to create user
async def create_user(db: Session,user_data:UserBase):
    try:
        user = User(**user_data.dict())
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"msg": "success", "user": user}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"User creation failed: {str(e)}")
    
#Function to read all the users
async def read_user(db:Session):
    db_user=db.query(User).all()
    return db_user

#Function to update the user details
async def update_user(db: Session, user_id:int, user_data:UserBase):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    try:
        user.name = user_data.name
        user.age = user_data.age
        user.hobby = user_data.hobby
        db.commit()
        db.refresh(user)
        return {"msg": "success", "user": user}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"User update failed: {str(e)}")
    

#Function to delete the user
async def delete_user(db: Session, user_id:int, user_data:UserBase):
    user=db.query(User).filter(User.user_id == user_id).first()

    try:
        if user:
            db.delete(user)
            db.commit()
            return {"msg":"user deleted successfully"}
        
    except Exception as e:
        db.rollback()
        raise HTTPException ("error while deleting the user")
    
