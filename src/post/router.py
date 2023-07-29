from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database import get_async_session
from src.models import User
from src.post import service, schemas
from src.auth.dependencies import oauth2_scheme

from src.post.dependencies import get_current_user_id

router = APIRouter(
    prefix="/jwt",
    tags=["Post"]
)

# Не работает нихуя сука бля
@router.post("/posts/", response_model=schemas.PostBase)
async def create_post(post: schemas.PostCreate, current_user: User = Depends(get_current_user_id), db: Session = Depends(get_async_session)):
    return await service.create_post(post, current_user, db)

# @router.post("/posts/", response_model=schemas.PostBase)
# async def create_post(post: schemas.PostCreate, current_user: User = Depends(get_current_user_id), db: Session = Depends(get_async_session)):
#     return await service.create_post(db, post, current_user)


# @router.get("/posts/{post_id}", response_model=schemas.Post)
# def read_post(post_id: int, db: Session = Depends(get_async_session)):
#     post = service.get_post_by_id(db, post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return post

# @router.put("/posts/{post_id}", response_model=schemas.Post)
# def update_post(
#     post_id: int,
#     post: schemas.PostUpdate,
#     current_user: User = Depends(get_current_user_id),
#     db: Session = Depends(get_async_session)
# ):
#     post_owner = service.get_post_by_id(db, post_id)
#     if not post_owner:
#         raise HTTPException(status_code=404, detail="Post not found")

#     if post_owner.author_id != current_user.id:
#         raise HTTPException(status_code=403, detail="You are not the owner of this post")

#     updated_post = service.update_post(db, post_owner, post)
#     return updated_post


# @router.delete("/posts/{post_id}", response_model=schemas.PostUpdate)
# def delete_post(
#     post_id: int,
#     post_owner: Post = Depends(is_post_owner),
#     db: Session = Depends(get_async_session)
# ):
#     service.delete_post(db, post_id)
#     return post_owner  # Return the deleted post owner or a suitable response model


