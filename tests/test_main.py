from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_bmi_success():
    response = client.get(
        "/bmi?weight=70&height=1.75"
    )

    assert response.status_code == 200
    assert response.json()["bmi"] == 22.86


def test_bmi_zero_height():
    response = client.get(
        "/bmi?weight=70&height=0"
    )

    assert response.status_code == 400


def test_bmi_negative_weight():
    response = client.get(
        "/bmi?weight=-10&height=1.75"
    )

    assert response.status_code == 400
