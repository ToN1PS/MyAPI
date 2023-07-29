from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.post.models import Post
from src.post.service import get_post_by_id

from  src.database import User, get_async_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user_id(current_user: User = Depends(get_async_session)):
    return current_user

def is_post_owner(post_user_id: int = Depends(get_current_user_id), post: Post = Depends(get_post_by_id)):
    if post_user_id != post.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions to perform this action.")
    return post
