from pydantic import BaseModel

class LikeBase(BaseModel):
    post_id: int
    user_id: int

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    id: int

    class Config:
        orm_mode = True

class DislikeBase(BaseModel):
    post_id: int
    user_id: int

class DislikeCreate(DislikeBase):
    pass

class Dislike(DislikeBase):
    id: int

    class Config:
        orm_mode = True
