from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import csv
import io
from datetime import datetime
from system_monitor import get_all_metrics, get_cpu_usage, get_memory_usage, get_disk_usage, get_network_latency

app = FastAPI(title="InfraScan - DevOps Monitoring Tool")

# Serve static files (our HTML page)
@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.get("/metrics")
async def get_metrics():
    """Get all system metrics"""
    return get_all_metrics()

@app.get("/metrics/cpu")
async def get_cpu():
    """Get CPU metrics only"""
    return get_cpu_usage()

@app.get("/metrics/memory") 
async def get_memory():
    """Get memory metrics only"""
    return get_memory_usage()

@app.get("/metrics/disk")
async def get_disk():
    """Get disk metrics only"""
    return get_disk_usage()

@app.get("/metrics/network")
async def get_network():
    """Get network metrics only"""
    return get_network_latency()

@app.get("/export/csv")
async def export_csv():
    """Export current metrics to CSV format"""
    metrics = get_all_metrics()
    
    # Flatten the nested dictionary for CSV
    flat_data = {
        'timestamp': metrics['timestamp'],
        'cpu_percent': metrics['cpu']['cpu_percent'],
        'cpu_count': metrics['cpu']['cpu_count'],
        'memory_total_gb': metrics['memory']['total_gb'],
        'memory_used_gb': metrics['memory']['used_gb'],
        'memory_available_gb': metrics['memory']['available_gb'],
        'memory_percent': metrics['memory']['percent'],
        'disk_total_gb': metrics['disk']['total_gb'],
        'disk_used_gb': metrics['disk']['used_gb'],
        'disk_free_gb': metrics['disk']['free_gb'],
        'disk_percent': metrics['disk']['percent'],
        'network_latency_ms': metrics['network']['latency_ms'],
        'network_status': metrics['network']['status']
    }
    
    # Create CSV content
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=flat_data.keys())
    writer.writeheader()
    writer.writerow(flat_data)
    
    csv_content = output.getvalue()
    output.close()
    
    return {
        "csv_data": csv_content,
        "filename": f"system_metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
