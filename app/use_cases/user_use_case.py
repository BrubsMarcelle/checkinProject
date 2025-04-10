from app.domain.repositories import UserRepository
from app.domain.models import User
from datetime import timedelta
from app.core.security import create_access_token

class UserUseCase:
    @staticmethod
    async def create_user(username: str, email: str, password: str):
        user = User(username=username, email=email, password=password)
        return await UserRepository.create_user(user)

    @staticmethod
    async def authenticate_user(username: str, password: str):
        user = await UserRepository.find_user_by_username(username)
        if user and user["password"] == password:
            access_token = create_access_token(
                data={"sub": str(user["_id"])},
                expires_delta=timedelta(hours=1)
            )
            return {"access_token": access_token, "token_type": "bearer"}
        return None
    
    @staticmethod
    async def get_user_id_by_username(username: str):
        user = await UserRepository.find_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        return str(user["_id"])