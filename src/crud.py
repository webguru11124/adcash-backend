from sqlalchemy.orm import Session
from typing import Optional
from . import models, schemas

def get_campaigns(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Campaign).offset(skip).limit(limit).all()

def get_campaign(db: Session, campaign_id: int):
    return db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()

def create_campaign(db: Session, campaign: schemas.CampaignCreate):
    db_campaign = models.Campaign(
        title=campaign.title,
        landing_page_url=campaign.landing_page_url,
        is_running=campaign.is_running
    )
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    for payout in campaign.payouts:
        db_payout = models.Payout(**payout.model_dump(), campaign_id=db_campaign.id)
        db.add(db_payout)
    db.commit()
    return db_campaign

def update_campaign_status(db: Session, campaign_id: int, is_running: bool):
    db_campaign = db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()
    if db_campaign:
        db_campaign.is_running = is_running
        db.commit()
        db.refresh(db_campaign)
    return db_campaign

def filter_campaigns(db: Session, title: Optional[str] = None, landing_page_url: Optional[str] = None, is_running: Optional[bool] = None, skip: int = 0, limit: int = 10):
    query = db.query(models.Campaign)
    if title:
        query = query.filter(models.Campaign.title.contains(title))
    if landing_page_url:
        query = query.filter(models.Campaign.landing_page_url.contains(landing_page_url))
    if is_running is not None:
        query = query.filter(models.Campaign.is_running == is_running)
    return query.offset(skip).limit(limit).all()

def delete_campaign(db: Session, campaign_id: int):
    db_campaign = db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()
    if db_campaign:
        db.delete(db_campaign)
        db.commit()