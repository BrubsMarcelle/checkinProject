from typing import List
from app.infra.database import db
from app.domain.models import User, CheckIn, Ranking
from datetime import datetime, timedelta
from app.domain.models import User

class UserRepository:
    @staticmethod
    async def create_user(user: User):
        result = await db.users.insert_one(user.dict())
        return result

    @staticmethod
    async def find_user_by_email(email: str):
        return await db.users.find_one({"email": email})

    @staticmethod
    async def find_user_by_username(username: str):
        return await db.users.find_one({"username": username})
    
    @staticmethod
    async def find_user_by_id(user_id: str):
        return await db.users.find_one({"_id": user_id})

class CheckInRepository:
    @staticmethod
    async def create_checkin(checkin: CheckIn):
        return await db.checkins.insert_one(checkin.dict())

    @staticmethod
    async def get_weekly_checkins():
        start_of_week = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=datetime.now().weekday())
        return await db.checkins.find({"timestamp": {"$gte": start_of_week}}).to_list(None)

class RankingRepository:
    @staticmethod
    async def update_ranking(ranking: Ranking):
        await db.rankings.update_one(
            {"user_id": ranking.user_id},
            {"$set": {"score": ranking.score}},
            upsert=True
        )