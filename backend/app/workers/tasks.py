from app.workers.celery_app import celery_app


@celery_app.task
def process_video_task(video_path: str):
    return f"Processing {video_path}"