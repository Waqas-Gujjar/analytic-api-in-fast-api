from typing import List,Optional
from pydantic import BaseModel


class List_Schema (BaseModel):
    id : int
    page : Optional[str] = ""
    description : Optional[str] = ""


class ListGetSchema(BaseModel):
    result : List[List_Schema]
    count : int

class ListCreateschema (BaseModel):
    page : str
    description : Optional[str] = ""
   

class ListUpdateSchema (BaseModel):
    page : Optional[str] = ""
    description : str
