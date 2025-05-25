from fastapi import APIRouter
import json

from .models import ( 
    List_Model,
    ListGetSchema,
    ListCreateschema,
    ListUpdateSchema 
    )


router = APIRouter()

@router.get("/")
def item_list() -> ListGetSchema:
    return {
        "result" :[
            {"id" : 1},
            {"id" : 2},
            {"id" : 3},
        ],
        "count" : 3 

    }


@router.post("/")
def item_create (payload:ListCreateschema) -> List_Model:
    data = payload.model_dump()
    return {"id":123,**data}

@router.get("/{item_id}")
def item_get (item_id:int) -> List_Model:

    return {"id": item_id}

@router.put("/{item_id}")
def item_update (item_id:int, payload:ListUpdateSchema) -> List_Model:
    data = payload.model_dump()
    return {"id": item_id,**data}