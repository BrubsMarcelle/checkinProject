from app.domain.repositories import CheckInRepository
from app.infra.email_services import send_email
from datetime import datetime

class AlertUseCase:
    @staticmethod
    async def send_alerts():
        today = datetime.now().strftime("%d/%m/%y")
        users_without_checkin = await CheckInRepository.get_users_without_checkin(today)
        for user in users_without_checkin:
            send_email(
                to_email=user["email"],
                subject="Alerta: Treinamento Cognitivo",
                body="Você ainda não realizou o check-in hoje. Não se esqueça de treinar!"
            )
        return {"message": f"Alerts sent to {len(users_without_checkin)} users"}