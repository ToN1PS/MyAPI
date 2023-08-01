# src/post/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from src.database import Base
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()


class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")
    likes = relationship("Like", back_populates="post")
    dislikes = relationship("Dislike", back_populates="post")

