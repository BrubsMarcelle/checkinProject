from fastapi import APIRouter
from app.use_cases.alert_use_case import AlertUseCase

router = APIRouter()

@router.post("/send-alerts")
async def send_alerts():
    result = await AlertUseCase.send_alerts()
    return result