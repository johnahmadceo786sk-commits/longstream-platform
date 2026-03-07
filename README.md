# LongStream Platform

LongStream is a high-capacity video streaming platform designed to support **3–5 hour video uploads** using chunked streaming (HLS).

## Core Features

- Long video uploads (up to 5 hours)
- HLS streaming (.m3u8 + segments)
- Real-time updates
- Searchable video library
- Watch or Download options
- Host dashboard for uploads
- Public viewing interface

## Architecture

Frontend
- Next.js

Backend
- FastAPI

Streaming
- HLS (FFmpeg)

Queue System
- Celery + Redis

Database
- PostgreSQL

Proxy
- Nginx

Storage
- Local storage or cloud object storage

## Default Host Account

Username: