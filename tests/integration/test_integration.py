import httpx

BASE_URL = "http://localhost:8000"


def test_service_is_healthy():
    resp = httpx.get(f"{BASE_URL}/health", timeout=5)
    assert resp.status_code == 200


def test_full_predict_flow():
    resp = httpx.post(
        f"{BASE_URL}/predict",
        json={"text": "will you deploy me?"},
        timeout=5,
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["prediction"] == "I Love You"
    assert body["model_version"] == "1.0.0"


def test_contract_is_enforced_over_the_wire():
    resp = httpx.post(f"{BASE_URL}/predict", json={"wrong": "field"}, timeout=5)
    assert resp.status_code == 422
