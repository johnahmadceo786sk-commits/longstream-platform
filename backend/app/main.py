from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, host, public, search, stream, download

app = FastAPI(
    title="LongStream Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(host.router, prefix="/host", tags=["Host"])
app.include_router(public.router, prefix="/public", tags=["Public"])
app.include_router(search.router, prefix="/search", tags=["Search"])
app.include_router(stream.router, prefix="/stream", tags=["Stream"])
app.include_router(download.router, prefix="/download", tags=["Download"])


@app.get("/")
def health_check():
    return {"status": "LongStream running"}