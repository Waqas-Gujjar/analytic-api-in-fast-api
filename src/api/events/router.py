from fastapi import APIRouter
from .schemas import ( 
    List_Schema,
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
def item_create (payload:ListCreateschema) -> List_Schema:
    print(payload)   
    return {"id":123}

@router.get("/{item_id}")
def item_get (item_id:int) -> List_Schema:

    return {"id": item_id}

@router.put("/{item_id}")
def item_update (item_id:int, payload:ListUpdateSchema) -> List_Schema:
    print(payload)
    return {"id": item_id}