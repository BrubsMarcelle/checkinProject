from app.domain.repositories import CheckInRepository
from app.domain.models import CheckIn
from datetime import datetime

class CheckInUseCase:
    @staticmethod
    async def register_checkin(user_id: str):
        timestamp = datetime.now()
        date = timestamp.strftime("%d/%m/%y")
        checkin = CheckIn(user_id=user_id, timestamp=timestamp, date=date)
        return await CheckInRepository.create_checkin(checkin)