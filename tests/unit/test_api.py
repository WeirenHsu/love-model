from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("./health")
    assert resp.status_code == 200


def test_predict_happy_path():
    resp = client.post("./predict", json={"text": ""})
    assert resp.status_code == 422


def test_predict_rejects_missing_field():
    resp = client.post("./predict", json={})
    assert resp.status_code == 422
