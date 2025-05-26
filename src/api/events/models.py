from typing import List ,Optional
from sqlmodel import SQLModel , Field 

from datetime import timezone, datetime
import sqlmodel

def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)

class list_model (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page : Optional[str] = ""
    description : Optional[str] = ""
    create_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False,
    )
    update_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False,
    )


class ListGetSchema(SQLModel):
    result : List[list_model]
    count : int

class ListCreateschema (SQLModel):
    page : str
    description : Optional[str] = ""



class ListUpdateSchema (SQLModel):
    description : str
    page : Optional[str] = ""