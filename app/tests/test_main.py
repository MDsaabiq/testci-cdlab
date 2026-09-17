from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/index")

    assert response.status_code == 200
    assert response.json()["app"] == "AI CI/CD Failure Investigator"


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "app": "AI CI/CD Failure Investigator",
    }
