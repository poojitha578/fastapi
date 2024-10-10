from fastapi import FastAPI
from controller.usercon import router
from db_configuration.config import engine
from db_configuration.db_model import Base

app=FastAPI()

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("table created successfully")
    except Exception as e:
        print(f"an error occuring while creating the table",{e})

#call the function to create the table
create_tables()
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI !"}