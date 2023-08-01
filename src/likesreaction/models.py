# src/post/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from src.database import Base
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

class Like(Base):
    __tablename__ = "likes"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="likes")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")

class Dislike(Base):
    __tablename__ = "dislikes"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="dislikes")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")