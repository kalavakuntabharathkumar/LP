from pydantic import BaseModel
class IncidentCreate(BaseModel): evidence:str
class IncidentOut(BaseModel):
    id:int; incident_type:str; severity:str; summary:str; evidence:str; status:str
    class Config: from_attributes=True
