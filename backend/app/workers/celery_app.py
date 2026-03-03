from celery import Celery
import os

celery = Celery(
    "longstream",
    broker=os.getenv("REDIS_URL", "redis://redis:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://redis:6379/0"),
)

celery.conf.task_routes = {
    "app.workers.tasks.process_video": {"queue": "video_queue"}
}