from fastapi import APIRouter,Depends,HTTPException
import json
from sqlmodel import Session,select
from api.db.sessions import get_session


from .models import ( 
    list_model,
    ListGetSchema,
    ListCreateschema,
    ListUpdateSchema 
    )


router = APIRouter()

@router.get("/",response_model =  ListGetSchema)
def item_list(session:Session = Depends(get_session))  :
    query = select(list_model)
    result = session.exec(query).all()
    return {
        "result" :result,
        "count" : len(result)

    }


@router.post("/",response_model =  list_model)
def item_create (payload:ListCreateschema,session:Session = Depends(get_session)):
    data = payload.model_dump()
    obj = list_model.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get("/{item_id}",response_model =  list_model)
def item_get (item_id:int,session:Session = Depends(get_session)) :
    query = select(list_model).where(list_model.id == item_id)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404,default="Data not Found")
    return result

@router.put("/{item_id}",response_model =  list_model)
def item_update (item_id:int, payload:ListUpdateSchema,session:Session = Depends(get_session)) :
    query = select(list_model).where(list_model.id == item_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404,detail="Data not Found")
    data = payload.model_dump()
    for k,v in data.items():
        if k == "id":
            continue
        setattr(obj,k,v)
        session.add(obj)
        session.commit()
        session.refresh(obj)
    return obj
    

@router.delete("/{item_id}")
def item_delete (item_id:int,session:Session = Depends(get_session)) :
    query = select(list_model).where(list_model.id == item_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404,detail="Data not Found")
    session.delete(obj)
    session.commit()
    return {"status":"ok","message":"Data Deleted Successfully"}