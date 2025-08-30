from pydantic import BaseModel
from typing import Optional

# Request schema: input features for prediction
class StartupStatusRequest(BaseModel):
    founded_at: int
    active_days: int
    first_funding_at: int
    last_funding_at: int
    funding_total_usd: float
    first_milestone_at: int
    last_milestone_at: int
    milestones: int
    relationships: int
    lng: float
    
    # One-hot encoded features for categories
    category_code: str

    # One-hot encoded features for countries
    country_code: str

# Response schema: prediction output
class StartupStatusResponse(BaseModel):
    predicted_status: str
