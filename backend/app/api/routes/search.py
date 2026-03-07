from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def search_videos(query: str):
    return {"query": query}