# 🖥️ InfraScan - DevOps System Monitoring Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **A modern, real-time system health monitoring solution with both web dashboard and CLI interfaces. Built to demonstrate DevOps automation, API development, and system monitoring expertise.**

## 🎯 Project Overview

InfraScan is a comprehensive system monitoring utility that showcases modern DevOps practices and full-stack development skills. It provides real-time insights into system performance through multiple interfaces, making it perfect for infrastructure monitoring, troubleshooting, and automated health checks.

**Why InfraScan?** This project demonstrates practical DevOps skills that are directly applicable to production environments - system monitoring, API design, automation scripting, and user-friendly dashboards.

## ✨ Key Features

### 🔍 **Comprehensive System Monitoring**
- **CPU Usage** - Real-time processor utilization and core count
- **Memory Analysis** - RAM usage, availability, and allocation tracking  
- **Disk Storage** - Space utilization and free capacity monitoring
- **Network Health** - Latency testing with visual status indicators
- **Process Management** - Total process count with top CPU/memory consumers

### 🌐 **Multi-Interface Architecture** 
- **Modern Web Dashboard** - Glassmorphism UI with auto-refresh capabilities
- **RESTful API** - JSON endpoints for integration with other tools
- **Command Line Tool** - Terminal-based monitoring for automation and scripting
- **CSV Export** - Data persistence for reporting and analysis

### ⚡ **Production-Ready Features**
- Cross-platform compatibility (Linux, macOS, Windows)
- Lightweight dependencies and minimal resource footprint
- Error handling and graceful degradation
- Responsive design for mobile and desktop access

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python 3.8+, FastAPI, Uvicorn |
| **System Monitoring** | psutil, subprocess, platform |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Data Processing** | CSV, JSON, argparse |
| **Architecture** | REST API, CLI Tools, MVC Pattern |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/zechariahcopelan/infrascan.git
cd infrascan

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the web application
python main.py
```

**Access the Dashboard:** Open http://localhost:8000 in your browser

### Command Line Usage

```bash
# View all system metrics
python cli.py

# Check specific components
python cli.py --cpu --memory
python cli.py --processes
python cli.py --network

# Export data for analysis
python cli.py --export-csv system_report.csv

# View help and options
python cli.py --help
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/` | GET | Web dashboard interface |
| `/metrics` | GET | Complete system metrics (JSON) |
| `/metrics/cpu` | GET | CPU usage only |
| `/metrics/memory` | GET | Memory statistics only |
| `/metrics/disk` | GET | Disk usage only |
| `/metrics/network` | GET | Network latency only |
| `/metrics/processes` | GET | Process information only |
| `/export/csv` | GET | CSV export of current metrics |

### Sample API Response
```json
{
  "timestamp": "2025-08-24T17:35:27.466339",
  "cpu": {"cpu_percent": 5.3, "cpu_count": 16},
  "memory": {"total_gb": 14.87, "used_gb": 10.48, "percent": 64.7},
  "disk": {"total_gb": 31.79, "used_gb": 21.16, "percent": 66.58},
  "network": {"latency_ms": 96.2, "status": "success"},
  "processes": {"total_processes": 441, "active_processes": 8}
}
```

## 🏗️ Architecture & Design Decisions

### **Modular Architecture**
- **`system_monitor.py`** - Core monitoring logic (separation of concerns)
- **`main.py`** - FastAPI web application and API routes
- **`cli.py`** - Command-line interface with argparse
- **`index.html`** - Modern glassmorphism UI with vanilla JavaScript

### **Key Design Patterns**
- **Single Responsibility** - Each module has a focused purpose
- **API-First Design** - CLI and web interface both consume the same monitoring functions
- **Error Handling** - Graceful degradation for network failures and permission issues
- **Cross-Platform** - Uses platform-specific commands for network testing

### **Performance Considerations**
- Minimal dependencies for fast startup
- Efficient data structures and caching
- Non-blocking network requests
- Configurable refresh intervals

## 🎨 User Interface

The web dashboard features a modern **glassmorphism design** with:
- **Real-time metrics** with auto-refresh functionality
- **Color-coded status indicators** for quick health assessment
- **Responsive grid layout** that adapts to different screen sizes
- **One-click CSV export** for data analysis
- **Process monitoring** with top resource consumers

## 📈 DevOps & Production Considerations

### **Monitoring Best Practices Demonstrated**
- Multi-dimensional metrics collection (CPU, memory, disk, network, processes)
- Historical data export capabilities
- API design for integration with monitoring platforms
- Command-line tools for automation and scripting

### **Scalability Features**
- Lightweight resource usage
- Stateless API design
- Configurable monitoring intervals
- Export capabilities for external analysis

### **Potential Integrations**
- Prometheus/Grafana for time-series data
- Alerting systems for threshold monitoring
- CI/CD pipelines for automated health checks
- Infrastructure as Code deployments

## 🔮 Future Enhancements

- [ ] **Historical Data Storage** - SQLite/PostgreSQL integration for trend analysis
- [ ] **Alert System** - Configurable thresholds with email/Slack notifications
- [ ] **Docker Support** - Containerization for easy deployment
- [ ] **Authentication** - JWT-based security for production environments
- [ ] **Metrics Dashboard** - Advanced charting with Chart.js or D3.js
- [ ] **Multi-Host Monitoring** - Remote system monitoring capabilities
- [ ] **Configuration Management** - YAML-based settings for different environments

## 🤝 Contributing

This project demonstrates industry best practices and is designed for educational and portfolio purposes. Contributions, suggestions, and feedback are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💼 About This Project

**Built by:** Zechariah Copeland  
**Website:** zechariahcopeland.com
**Portfolio:** https://github.com/zechariahcopelan/InfraScan  
**LinkedIn:** www.linkedin.com/in/zechariah-copeland-b3b4b1199  
**Email:** zechariahcopelan@gmail.com

This project was developed to demonstrate:
- **DevOps Engineering Skills** - System monitoring, automation, infrastructure management
- **Full-Stack Development** - Backend APIs, frontend interfaces, database design
- **Python Expertise** - Advanced libraries, CLI tools, web frameworks
- **Production Mindset** - Error handling, scalability, documentation, testing

---

*⭐ If this project demonstrates the kind of technical skills you're looking for, let's connect! I'm passionate about building robust, scalable solutions that solve real-world problems.*
