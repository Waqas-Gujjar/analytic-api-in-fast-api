from typing import List
from pydantic import BaseModel


class List_Schema (BaseModel):
    id : int


class ListGetSchema(BaseModel):
    result : List[List_Schema]
    count : int

class ListCreateschema (BaseModel):
    page : str


class ListUpdateSchema (BaseModel):
    description : str