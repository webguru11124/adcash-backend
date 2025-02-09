from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_campaign():
    response = client.post(
        "/campaigns/",
        json={
            "title": "Test Campaign",
            "landing_page_url": "http://example.com",
            "is_running": True,
            "payouts": [
                {"amount": 100, "country": "US"},
                {"amount": 200, "country": "CA"}
            ]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Campaign"
    assert data["landing_page_url"] == "http://example.com"
    assert data["is_running"] == True
    assert len(data["payouts"]) == 2

def test_read_campaigns():
    response = client.get("/campaigns/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_read_campaign():
    response = client.get("/campaigns/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Campaign"

def test_update_campaign_status():
    response = client.put("/campaigns/1/status", params={"is_running": False})
    assert response.status_code == 200
    data = response.json()
    assert data["is_running"] == False

def test_filter_campaigns():
    response = client.get("/campaigns/filter", params={"title": "Test", "is_running": False})
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
