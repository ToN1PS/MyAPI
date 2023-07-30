from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.auth.utils import get_user_db

from src.database import get_async_session
from src.models import User
from src.post import service, schemas
from src.auth.config import current_user


router = APIRouter(
    prefix="/jwt",
    tags=["Post"]
)


@router.post("/posts/", response_model=schemas.PostBase)
async def create_post(post: schemas.PostCreate, current_user: User = Depends(current_user), db: Session = Depends(get_async_session)):
    
    return await service.create_post(post, current_user.id, db)


@router.get("/posts/{post_id}", response_model=schemas.Post)
async def read_post(post_id: int, db: Session = Depends(get_async_session)):
    post_data = await service.get_post_by_id(post_id, db)
    if not post_data:
        raise HTTPException(status_code=404, detail="Post not found")
    return schemas.Post(**post_data)

@router.put("/posts/{post_id}", response_model=schemas.Post)
async def update_post(post_id: int, post_update_data: schemas.PostUpdate, db: Session = Depends(get_async_session)):
    post = await service.get_post_by_id(post_id, db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Преобразуем модель `PostUpdate` в словарь, чтобы передать его в функцию обновления
    post_update_dict = post_update_data.model_dump(exclude_unset=True)
    
    await service.update_post_by_id(post_id, post_update_dict, db)
    
    # Возвращаем обновленный пост
    return await service.get_post_by_id(post_id, db)


@router.delete("/posts/{post_id}", response_model=schemas.Post)
async def delete_post(
    post_id: int,
    current_user: User = Depends(current_user),
    db: Session = Depends(get_async_session),
):
    post = await service.get_post_by_id(post_id, db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Проверяем, что текущий пользователь является владельцем поста
    if current_user.id != post.user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    await service.delete_post_by_id(post_id, db)
    
    # Возвращаем удаленный пост
    return post



