# src/post/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from src.database import Base

metadata = MetaData()

class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    # Внешний ключ для связи с таблицей users
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
