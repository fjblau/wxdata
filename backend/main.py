from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import weather

app = FastAPI(title="Weather Data API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather.router, prefix="/api")


@app.get("/health")
async def health():
    return {"status": "ok"}
