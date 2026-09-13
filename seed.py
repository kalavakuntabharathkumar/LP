from app.database import Base,SessionLocal,engine
from app.models import Incident
Base.metadata.create_all(bind=engine)
samples=[('disk','high','Disk capacity threshold exceeded.','Filesystem reports disk full.'),('memory','high','Memory pressure detected.','Application reports out of memory.'),('permission','medium','Access policy failure detected.','Permission denied while opening log.'),('database','high','Database connectivity issue detected.','Database connection refused.'),('service','high','Application process failure detected.','Service down after process exited.')]
db=SessionLocal()
try:
    for t,s,summary,evidence in samples:db.add(Incident(incident_type=t,severity=s,summary=summary,evidence=evidence))
    db.commit()
finally:db.close()
print('Seeded LinuxPulse sample incidents.')
