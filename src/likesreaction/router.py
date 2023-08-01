from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from likesreaction.models import Like


from src.database import get_async_session
from src.models import User
from src.post.service import get_post_by_id
from src.auth.config import current_user


router = APIRouter(
    prefix="/jwt",
    tags=["Likes and Dislikes"]
)



@router.post("/posts/{post_id}/like/")
async def like_post(post_id: int, db: Session = Depends(get_async_session), current_user: User = Depends(current_user)):
    
    post = await get_post_by_id(post_id, db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id == current_user.id:
        raise HTTPException(status_code=400, detail="Users cannot like their own posts")
    
    
    like = Like(post_id=post_id, user_id=current_user.id)
    db.add(like)
    db.commit()
    return {"message": "Post liked successfully"}