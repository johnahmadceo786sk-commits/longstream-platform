from pydantic import BaseModel


class VideoCreate(BaseModel):
    title: str
    description: str


class VideoResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True