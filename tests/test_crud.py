import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src import crud, models, schemas

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_campaign(db):
    campaign_data = schemas.CampaignCreate(
        title="Test Campaign",
        landing_page_url="http://example.com",
        is_running=True,
        payouts=[
            schemas.PayoutCreate(amount=100, country="US"),
            schemas.PayoutCreate(amount=200, country="CA")
        ]
    )
    campaign = crud.create_campaign(db, campaign=campaign_data)
    assert campaign.title == "Test Campaign"
    assert campaign.landing_page_url == "http://example.com"
    assert campaign.is_running == True
    assert len(campaign.payouts) == 2

def test_get_campaign(db):
    campaign = crud.get_campaign(db, campaign_id=1)
    assert campaign is not None
    assert campaign.title == "Test Campaign"

def test_get_campaigns(db):
    campaigns = crud.get_campaigns(db, skip=0, limit=10)
    assert len(campaigns) > 0

def test_update_campaign_status(db):
    campaign = crud.update_campaign_status(db, campaign_id=1, is_running=False)
    assert campaign.is_running == False

def test_filter_campaigns(db):
    campaigns = crud.filter_campaigns(db, title="Test", is_running=False)
    assert len(campaigns) > 0
