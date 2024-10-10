
from pydantic import BaseModel


class item(BaseModel):
    _id:int
    name: str
    age:int
    Hobby:str
    DOB:str

