import psycopg2 
from sqlalchemy import create_engine,text,Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import Column,Integer,String
from db_configuration.db_model import User

SQLALCHEMY_DATABASE_URL='postgresql://postgres:Password@172.16.0.103:5432/test'

try:
    # forming connection
    engine=create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
    User
    print('database connected sucessfully')
    
except SQLAlchemyError as e:
    print("An error occurred:", e)
    
 

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

   # class User(Base):
    #     __tablename__ = 'user_table'
    #     user_id = Column(Integer, primary_key=True, autoincrement=True)
    #     username = Column(String(50), nullable=False)
    #     email = Column(String(100), nullable=False)