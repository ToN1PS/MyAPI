from sqlalchemy.orm import Session
from src.post.schemas import PostCreate
from fastapi import Depends
from src.database import get_async_session
from src.post.models import Post

def get_post_by_id(post_id: int, db: Session = Depends(get_async_session)) -> Post:
    return db.query(Post).filter(Post.id == post_id).first()


async def create_post(post: PostCreate, user_id: int, db: Session = Depends(get_async_session)) -> Post:
    
    new_post = Post(
        title=post.title,
        content=post.content,
        user_id = user_id
    )
    # Добавляем объект поста в сессию
    db.add(new_post)

    # Сохраняем изменения в базу данных и ожидаем выполнения операции
    await db.commit()

    # Освежаем состояние объекта поста, чтобы он содержал значения из базы данных (например, ID)
    await db.refresh(new_post)

    # Возвращаем созданный пост
    return new_post
    
 