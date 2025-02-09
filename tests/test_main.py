import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def setup_module(module):
    from src.database import Base, engine
    Base.metadata.create_all(bind=engine)

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

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1

def test_multiplication():
    assert 2 * 2 == 4

def test_division():
    assert 4 / 2 == 2