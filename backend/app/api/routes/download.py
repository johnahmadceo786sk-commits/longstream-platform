from fastapi import APIRouter

router = APIRouter()


@router.get("/{video_id}")
def download_video(video_id: int):
    return {"download_video": video_id}