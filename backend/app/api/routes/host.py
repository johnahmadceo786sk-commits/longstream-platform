from app.workers.tasks import process_video
import os

from app.database.models import video

process_video.delay(video.id, "/path/to/uploaded/file")

UPLOAD_DIR = "storage/raw"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_video(
    title: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    host: User = Depends(get_current_host)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    video = Video(
        title=title,
        original_filename=file.filename,
        stored_name=file.filename,
        uploaded_by=host.id
    )

    db.add(video)
    db.commit()
    db.refresh(video)

    # Send to background worker
    process_video.delay(video.id, file_path)

    return {"message": "Video uploaded. Processing started."}