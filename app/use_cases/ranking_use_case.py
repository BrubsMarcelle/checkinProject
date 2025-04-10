from app.domain.repositories import CheckInRepository, RankingRepository
from app.domain.models import Ranking
from datetime import datetime, timedelta

class RankingUseCase:
    @staticmethod
    async def calculate_weekly_ranking():
        # Obter check-ins semanais
        weekly_checkins = await CheckInRepository.get_weekly_checkins()

        # Calcular pontuação dos usuários
        user_scores = {}
        for checkin in weekly_checkins:
            user_id = str(checkin["user_id"])  # Converter ObjectId para string
            user_scores[user_id] = user_scores.get(user_id, 0) + 20  # 20 pontos por check-in

        # Ordenar por pontuação
        sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
        ranking_list = [{"user_id": user_id, "score": score} for user_id, score in sorted_users]

        # Atualizar ranking no banco de dados
        for rank in ranking_list:
            ranking = Ranking(user_id=rank["user_id"], score=rank["score"])
            await RankingRepository.update_ranking(ranking)

        return ranking_list