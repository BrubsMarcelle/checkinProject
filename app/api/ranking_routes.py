from fastapi import APIRouter, Depends
from app.use_cases.ranking_use_case import RankingUseCase
from app.core.security import get_current_user

router = APIRouter()

@router.get("/ranking")
async def get_weekly_ranking(current_user: str = Depends(get_current_user)):
    ranking = await RankingUseCase.calculate_weekly_ranking()
    return {"ranking": ranking}