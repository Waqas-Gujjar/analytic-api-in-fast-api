from typing import List ,Optional
from sqlmodel import SQLModel , Field


class List_Model (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page : Optional[str] = ""
    description : Optional[str] = ""


class ListGetSchema(SQLModel):
    result : List[List_Model]
    count : int

class ListCreateschema (SQLModel):
    page : str
    description : Optional[str] = ""



class ListUpdateSchema (SQLModel):
    description : str
    page : Optional[str] = ""