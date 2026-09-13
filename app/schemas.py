from pydantic import BaseModel, Field

class IncidentCreate(BaseModel):
    evidence: str = Field(min_length=3)
    source: str = 'health-check'
    assigned_to: str = 'support-engineer'

class IncidentUpdate(BaseModel):
    status: str | None = None
    assigned_to: str | None = None
    resolution_notes: str | None = None

class IncidentOut(BaseModel):
    id:int; incident_type:str; severity:str; summary:str; evidence:str; status:str; assigned_to:str; source:str; resolution_notes:str
    class Config: from_attributes=True
