from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, declared_attr, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer, Column, TIMESTAMP, ForeignKey
import datetime 

from src.auth.models import role

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeMeta = declarative_base()

class User(SQLAlchemyBaseUserTableUUID, Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))

    # Columns with mapped_column decorator
    hashed_password = mapped_column(String(length=1024), nullable=False)
    is_active = mapped_column(Boolean, default=True, nullable=False)
    is_superuser = mapped_column(Boolean, default=False, nullable=False)
    is_verified = mapped_column(Boolean, default=False, nullable=False)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")
    likes = relationship("Like", back_populates="post")
    dislikes = relationship("Dislike", back_populates="post")


class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="likes")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
    
class Dislike(Base):
    __tablename__ = "dislikes"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="dislikes")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
