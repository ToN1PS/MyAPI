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
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    
    

    def __repr__(self):
        return f"<Post(title={self.title}, user_id={self.user_id})>"
