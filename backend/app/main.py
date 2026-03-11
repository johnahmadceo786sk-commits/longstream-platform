from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

UPLOAD_DIR = "videos"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.get("/dashboard")
def host_dashboard():
    return {"message": "Host dashboard"}


@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return {
        "message": "Video uploaded successfully",
        "filename": file.filename
    }