from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import null
from app.models.schemas import UpgradePost
from app.models.dao import PostsDAO


router = APIRouter(
    prefix="/posts", 
    tags=["Посты"],
)



@router.post("")
async def new_post(text: str, like: bool):
    result = await PostsDAO.get_new_post(text, like)
    return result


@router.get("")
async def get_all_post():
    result = await PostsDAO.find_all()
    return result

@router.post("/{id}")
async def get_one_id(id: int):
    result = await PostsDAO.find_by_id(id)
    if result == None:
        return {"message": "Errore"}
    return result

@router.delete("/{id}")
async def delete_post_by_id(id: int):
    result = await PostsDAO.delete_post(id)
    if result:
        return {"message": "Successful"}
    return {"message": "No successful"}

@router.put("/{id}", response_model=UpgradePost)
async def upgrade_post(id: int, text: UpgradePost):
    result = await PostsDAO.upgrade_post(id, text)
    if result == 0:
        return {"message": "Успешно обновлено!"}
    return result

@router.post("/{id}/like")
async def get_like(id: int, like: bool):
    result = await PostsDAO.get_like(id, like)
    if result is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if result == 0:
        return {"message": "Successful"}
    return result

@router.delete("/{id}/like")
async def delete_like_for_id(id: int):
    result = await PostsDAO.delete_like_for_id(id)
    if result:
        return {"message": "Like updated"}
    return {"message": "Failed to update like"}

