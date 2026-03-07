from fastapi import APIRouter

router = APIRouter()


@router.get("/dashboard")
def host_dashboard():
    return {"message": "Host dashboard"}