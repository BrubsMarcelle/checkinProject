from fastapi import APIRouter, Depends, HTTPException
from app.use_cases.checkin_use_case import CheckInUseCase
from app.core.security import get_current_user

router = APIRouter()

@router.post("/checkin")
async def register_checkin(current_user: str = Depends(get_current_user)):
    """
    Registra um check-in para o usuário autenticado.
    """
    result = await CheckInUseCase.register_checkin(user_id=current_user)
    if result:
        return {"message": "Check-in registered successfully", "checkin_id": str(result.inserted_id)}
    raise HTTPException(status_code=500, detail="Failed to register check-in")