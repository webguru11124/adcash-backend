from pydantic import BaseModel
from typing import List, Optional

class PayoutBase(BaseModel):
    amount: int
    country: str

class PayoutCreate(PayoutBase):
    pass

class Payout(PayoutBase):
    id: int
    campaign_id: int

    class Config:
        orm_mode = True

class CampaignBase(BaseModel):
    title: str
    landing_page_url: str
    is_running: Optional[bool] = False

class CampaignCreate(CampaignBase):
    payouts: List[PayoutCreate]

class Campaign(CampaignBase):
    id: int
    payouts: List[Payout]

    class Config:
        orm_mode = True

class CampaignStatusUpdate(BaseModel):
    is_running: bool