from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    # Дополнительные поля, если необходимо, могут быть добавлены здесь
    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

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
    
    def __repr__(self):
        return f"<Post(title={self.title}, user_id={self.owner_id})>"

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
