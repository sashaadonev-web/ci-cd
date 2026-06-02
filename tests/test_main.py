from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_calculate_bmi_success():
    # Проверяем расчет для человека весом 70 кг и ростом 1.75 м
    response = client.get("/bmi?weight=70&height=1.75")
    assert response.status_code == 200
    assert response.json()["bmi"] == 22.86
