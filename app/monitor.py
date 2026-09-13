import socket
from dataclasses import dataclass
import psutil
@dataclass
class HealthSnapshot:
    cpu_percent:float; memory_percent:float; disk_percent:float; process_count:int; port_8000_open:bool
def port_is_open(host='127.0.0.1',port=8000,timeout=.15):
    s=socket.socket();s.settimeout(timeout)
    try:return s.connect_ex((host,port))==0
    finally:s.close()
def collect_health(path='/'):
    try: disk=psutil.disk_usage(path).percent
    except Exception: disk=0.0
    return HealthSnapshot(psutil.cpu_percent(interval=.15),psutil.virtual_memory().percent,disk,len(psutil.pids()),port_is_open())
def classify_incident(s):
    if s.disk_percent>=90:return 'disk','high',f'Disk usage is {s.disk_percent:.1f}%.'
    if s.memory_percent>=90:return 'memory','high',f'Memory usage is {s.memory_percent:.1f}%.'
    if s.cpu_percent>=90:return 'service','high',f'CPU usage is {s.cpu_percent:.1f}%.'
    if not s.port_8000_open:return 'service','medium','Application port 8000 is not reachable.'
    return 'healthy','low','No threshold-based application incident detected.'
def classify_text_incident(evidence):
    t=evidence.lower()
    if any(x in t for x in ('disk full','no space left','storage full')):return 'disk','high'
    if any(x in t for x in ('out of memory','oom','memory exhausted')):return 'memory','high'
    if any(x in t for x in ('permission denied','forbidden')):return 'permission','medium'
    if any(x in t for x in ('database','db connection','connection refused')):return 'database','high'
    if any(x in t for x in ('service down','process exited','port closed')):return 'service','high'
    return 'unknown','medium'
