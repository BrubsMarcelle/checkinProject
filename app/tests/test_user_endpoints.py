import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_register_user(mocker):
    mocker.patch("app.use_cases.user_use_case.UserUseCase.create_user", return_value={"inserted_id": "mock_id"})
    response = client.post("/register", json={"username": "test", "email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json()["user_id"] == "mock_id"