from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from app.use_cases.user_use_case import UserUseCase

router = APIRouter()
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register_user(username: str, email: str, password: str):
    result = await UserUseCase.create_user(username, email, password)
    return {"message": "User created successfully", "user_id": str(result.inserted_id)}


@router.post("/login")
async def login(request: LoginRequest):
    user = await UserUseCase.authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

@router.get("/user-id/{username}")
async def get_user_id(username: str):
    try:
        user_id = await UserUseCase.get_user_id_by_username(username)
        return {"username": username, "user_id": user_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))