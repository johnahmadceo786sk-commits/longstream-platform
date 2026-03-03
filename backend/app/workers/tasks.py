import os
from app.workers.celery_app import celery
from app.services.video_processor import VideoProcessor
from app.services.s3_service import S3Service
from app.database.session import SessionLocal
from app.database.models.video import Video

@celery.task(name="app.workers.tasks.process_video")
def process_video(video_id: int, file_path: str):
    db = SessionLocal()

    try:
        video = db.query(Video).filter(Video.id == video_id).first()
        if not video:
            return

        output_dir = f"/tmp/hls_{video_id}"

        # Convert to HLS
        playlist_path = VideoProcessor.convert_to_hls(file_path, output_dir)

        # Upload HLS files to S3
        s3 = S3Service()
        for file_name in os.listdir(output_dir):
            full_path = os.path.join(output_dir, file_name)
            s3_key = f"hls/{video_id}/{file_name}"
            s3.upload_file(full_path, s3_key)

        # Save HLS master playlist URL
        video.hls_path = f"hls/{video_id}/playlist.m3u8"
        db.commit()

    except Exception as e:
        print("Video processing failed:", e)

    finally:
        db.close()