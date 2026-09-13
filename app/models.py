from datetime import datetime
from sqlalchemy import DateTime,Integer,String,Text
from sqlalchemy.orm import Mapped,mapped_column
from .database import Base

class Incident(Base):
    __tablename__='incidents'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    incident_type:Mapped[str]=mapped_column(String(50))
    severity:Mapped[str]=mapped_column(String(20))
    summary:Mapped[str]=mapped_column(Text)
    evidence:Mapped[str]=mapped_column(Text)
    status:Mapped[str]=mapped_column(String(20),default='open')
    assigned_to:Mapped[str]=mapped_column(String(120),default='support-engineer')
    source:Mapped[str]=mapped_column(String(30),default='health-check')
    resolution_notes:Mapped[str]=mapped_column(Text,default='')
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
