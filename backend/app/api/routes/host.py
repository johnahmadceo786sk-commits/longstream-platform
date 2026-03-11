from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

UPLOAD_FOLDER = "videos"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/dashboard")
def host_dashboard():
    return {"message": "Host dashboard"}


@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "message": "Video uploaded successfully",
        "filename": file.filename
    }