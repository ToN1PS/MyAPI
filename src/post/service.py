from sqlalchemy.orm import Session
from src.post.schemas import PostCreate
from fastapi import Depends
from src.database import get_async_session
from src.post.models import Post
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy import update

async def get_post_by_id(post_id: int, db: AsyncSession) -> dict:
    # Создаем селекторный запрос по идентификатору поста
    stmt = select(Post).where(Post.id == post_id)
    # Исполняем запрос и получаем результат
    result = await db.execute(stmt)
    post_data = result.scalar_one_or_none()
    return post_data.__dict__ if post_data else None

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
    
async def update_post_by_id(post_id: int, post_update_data: dict, db: AsyncSession):
    # Создаем обновляющий запрос по идентификатору поста
    stmt = update(Post).where(Post.id == post_id).values(post_update_data)
    # Исполняем запрос
    await db.execute(stmt)
    # Коммитим изменения
    await db.commit()