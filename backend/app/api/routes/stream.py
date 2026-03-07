from fastapi import APIRouter

router = APIRouter()


@router.get("/{video_id}")
def stream_video(video_id: int):
    return {"stream_video": video_id}