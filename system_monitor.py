import psutil
import subprocess
import platform
from datetime import datetime


def get_cpu_usage():
    """Get CPU usage percentage"""
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_count": psutil.cpu_count()
    }


def get_memory_usage():
    """Get memory usage info"""
    memory = psutil.virtual_memory()
    return {
        "total_gb": round(memory.total / (1024**3), 2),
        "available_gb": round(memory.available / (1024**3), 2),
        "used_gb": round(memory.used / (1024**3), 2),
        "percent": memory.percent
    }


def get_disk_usage():
    """Get disk usage for root directory"""
    disk = psutil.disk_usage('/')
    return {
        "total_gb": round(disk.total / (1024**3), 2),
        "used_gb": round(disk.used / (1024**3), 2),
        "free_gb": round(disk.free / (1024**3), 2),
        "percent": round((disk.used / disk.total) * 100, 2)
    }


def get_network_latency(host="8.8.8.8"):
    """Get network latency by pinging a host"""
    try:
        if platform.system().lower() == "windows":
            cmd = ["ping", "-n", "1", host]
        else:
            cmd = ["ping", "-c", "1", host]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            # Simple parsing - look for time= in output
            output = result.stdout
            if "time=" in output:
                time_str = output.split("time=")[1].split("ms")[0].strip()
                return {"latency_ms": float(time_str), "status": "success"}
        
        return {"latency_ms": None, "status": "failed"}
    
    except Exception:
        return {"latency_ms": None, "status": "error"}


def get_process_info():
    """Get process count and top processes by CPU and memory"""
    processes = []
    
    # Get all processes with their info
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Skip processes we can't access
            continue
    
    # Filter out processes with 0% CPU (to get more meaningful top processes)
    active_processes = [p for p in processes if p['cpu_percent'] and p['cpu_percent'] > 0]
    
    # Sort by CPU and memory usage
    top_cpu = sorted(active_processes, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:3]
    top_memory = sorted(processes, key=lambda x: x['memory_percent'] or 0, reverse=True)[:3]
    
    return {
        "total_processes": len(processes),
        "active_processes": len(active_processes),
        "top_cpu": [
            {
                "name": p['name'],
                "pid": p['pid'],
                "cpu_percent": round(p['cpu_percent'] or 0, 2)
            } for p in top_cpu
        ],
        "top_memory": [
            {
                "name": p['name'], 
                "pid": p['pid'],
                "memory_percent": round(p['memory_percent'] or 0, 2)
            } for p in top_memory
        ]
    }


def get_all_metrics():
    """Get all system metrics in one call"""
    return {
        "timestamp": datetime.now().isoformat(),
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "network": get_network_latency(),
        "processes": get_process_info()
    }
