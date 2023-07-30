from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int


class PostCreate(PostBase):
    title: str
    content: str
    user_id: int


class PostUpdate(PostBase):
    pass

class Post(PostBase):
    title: str
    content: str
    user_id: int
    
    class Config:
        from_attributes = True
