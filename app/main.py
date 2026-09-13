from pathlib import Path
from fastapi import Depends,FastAPI,HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.orm import Session
from .database import Base,engine,get_db
from .models import Incident
from .monitor import classify_incident,classify_text_incident,collect_health
from .schemas import IncidentCreate,IncidentOut
Base.metadata.create_all(bind=engine)
app=FastAPI(title='LinuxPulse API',version='1.0.0')
STATIC_DIR=Path(__file__).resolve().parent.parent/'static'
app.mount('/static',StaticFiles(directory=STATIC_DIR),name='static')
@app.get('/',include_in_schema=False)
def home():return FileResponse(STATIC_DIR/'index.html')
@app.get('/api/health')
def health():
    s=collect_health();t,severity,summary=classify_incident(s)
    return {'cpu_percent':s.cpu_percent,'memory_percent':s.memory_percent,'disk_percent':s.disk_percent,'process_count':s.process_count,'port_8000_open':s.port_8000_open,'incident_type':t,'severity':severity,'summary':summary}
@app.get('/api/incidents',response_model=list[IncidentOut])
def list_incidents(db:Session=Depends(get_db)):return db.scalars(select(Incident).order_by(Incident.id.desc())).all()
@app.post('/api/incidents',response_model=IncidentOut)
def create_incident(payload:IncidentCreate,db:Session=Depends(get_db)):
    t,severity=classify_text_incident(payload.evidence);i=Incident(incident_type=t,severity=severity,summary=f'Classified as {t} incident.',evidence=payload.evidence)
    db.add(i);db.commit();db.refresh(i);return i
@app.post('/api/incidents/{incident_id}/resolve',response_model=IncidentOut)
def resolve_incident(incident_id:int,db:Session=Depends(get_db)):
    i=db.get(Incident,incident_id)
    if not i:raise HTTPException(404,'Incident not found')
    i.status='resolved';db.commit();db.refresh(i);return i
