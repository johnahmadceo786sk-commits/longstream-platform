from pydantic import BaseModel
from typing import Optional

class VideoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class VideoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    duration: Optional[int]
    size: Optional[int]

    class Config:
        orm_mode = True