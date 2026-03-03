from app.services.websocket_manager import manager

class NotificationService:

    @staticmethod
    async def notify_new_video(video_id: int, title: str):
        await manager.broadcast({
            "event": "NEW_VIDEO",
            "video_id": video_id,
            "title": title
        })