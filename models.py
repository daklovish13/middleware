from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Nudge(BaseModel):
    type: Optional[str]  
    source_id: Optional[str]
    sent_at: Optional[datetime] = None
    seen_at: Optional[datetime] = None
    call_rm_at: Optional[datetime] = None
    will_pay_at: Optional[datetime] = None
    engagement: Optional[str] = None
    feedback: Optional[str] = None
    additional_feedback: Optional[str] = None

class Customer(BaseModel):
    CIN: str
    customer_name: str
    initial_churn: Optional[bool] = None
    latest_churn: Optional[bool] = None
    RM_ID: Optional[str] = None
    RM_Name: Optional[str] = None
    RM_Contact: Optional[str] = None
    Avatar_ID: Optional[str] = None  
    Voice_ID: Optional[str] = None
    nudges: Optional[List[Nudge]] = []
    Campaign_ID: Optional[str] = None
    Stage: Optional[str] = None  
