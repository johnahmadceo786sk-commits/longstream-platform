from fastapi import APIRouter

router = APIRouter()


@router.get("/videos")
def list_videos():
    return {"videos": []}