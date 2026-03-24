from fastapi import APIRouter

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("")
async def get_weather(location: str):
    return {"location": location, "data": None}
