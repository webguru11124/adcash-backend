import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
from src import models, schemas, crud

def init_db(db: Session):
    # Create initial test data
    campaigns = [
        schemas.CampaignCreate(
            title="Initial Campaign",
            landing_page_url="http://example.com",
            is_running=True,
            payouts=[
                schemas.PayoutCreate(amount=100, country="US"),
                schemas.PayoutCreate(amount=200, country="CA")
            ]
        ),
        schemas.CampaignCreate(
            title="Second Campaign",
            landing_page_url="http://example.org",
            is_running=False,
            payouts=[
                schemas.PayoutCreate(amount=150, country="UK"),
                schemas.PayoutCreate(amount=250, country="AU")
            ]
        ),
        schemas.CampaignCreate(
            title="Third Campaign",
            landing_page_url="http://example.net",
            is_running=True,
            payouts=[
                schemas.PayoutCreate(amount=300, country="IN"),
                schemas.PayoutCreate(amount=400, country="DE")
            ]
        )
    ]

    for campaign_data in campaigns:
        crud.create_campaign(db, campaign=campaign_data)

if __name__ == "__main__":
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()
