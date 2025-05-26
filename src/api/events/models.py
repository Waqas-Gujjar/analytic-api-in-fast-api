from typing import List ,Optional
from sqlmodel import SQLModel , Field


class list_model (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page : Optional[str] = ""
    description : Optional[str] = ""


class ListGetSchema(SQLModel):
    result : List[list_model]
    count : int

class ListCreateschema (SQLModel):
    page : str
    description : Optional[str] = ""



class ListUpdateSchema (SQLModel):
    description : str
    page : Optional[str] = ""