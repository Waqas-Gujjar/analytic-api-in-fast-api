from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def item_list():
    return {
        "item" : [1,2,3]
    }