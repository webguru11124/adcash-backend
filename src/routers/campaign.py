from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/campaigns",
    tags=["campaigns"],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Campaign)
def create_campaign(campaign: schemas.CampaignCreate, db: Session = Depends(get_db)):
    return crud.create_campaign(db=db, campaign=campaign)

@router.get("/", response_model=List[schemas.Campaign])
def read_campaigns(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    campaigns = crud.get_campaigns(db, skip=skip, limit=limit)
    return campaigns

@router.get("/filter", response_model=List[schemas.Campaign])
def filter_campaigns(
    title: Optional[str] = Query(None),
    landing_page_url: Optional[str] = Query(None),
    is_running: Optional[bool] = Query(None),
    skip: int = Query(0),
    limit: int = Query(10),
    db: Session = Depends(get_db)
):
    # Convert empty strings to None
    if title == "":
        title = None
    if landing_page_url == "":
        landing_page_url = None

    campaigns = crud.filter_campaigns(
        db, title=title, landing_page_url=landing_page_url, is_running=is_running, skip=skip, limit=limit
    )
    return campaigns

@router.get("/{campaign_id}", response_model=schemas.Campaign)
def read_campaign(campaign_id: int, db: Session = Depends(get_db)):
    db_campaign = crud.get_campaign(db, campaign_id=campaign_id)
    if db_campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaign

@router.put("/{campaign_id}/status", response_model=schemas.Campaign)
def update_campaign_status(campaign_id: int, status_update: schemas.CampaignStatusUpdate, db: Session = Depends(get_db)):
    db_campaign = crud.update_campaign_status(db, campaign_id=campaign_id, is_running=status_update.is_running)
    if db_campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaign

@router.delete("/{campaign_id}", response_model=schemas.Campaign)
def delete_campaign(campaign_id: int, db: Session = Depends(get_db)):
    db_campaign = crud.get_campaign(db, campaign_id=campaign_id)
    if db_campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    crud.delete_campaign(db, campaign_id=campaign_id)
    return db_campaign