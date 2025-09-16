# Problem Statement 2: System Monitoring & App Health Checker

## 📂 Project Structure
```
problem-statement-2/
├── health_monitor.py        # System Health Monitoring
├── app_health_checker.py    # Application Health Checker
├── logs/
│   ├── system_health.log
│   └── app_health.log
├── config.json              # Configurable thresholds and app URL
└── README.md
```

---

## 🚀 Scripts

### 1️⃣ System Health Monitoring (`health_monitor.py`)
- Monitors:
  - CPU usage
  - Memory usage
  - Disk space
- Logs alerts when thresholds are exceeded.

**Run:**
```bash
python3 health_monitor.py
```

### 2️⃣ Application Health Checker (`app_health_checker.py`)
- Checks if application is UP/DOWN via HTTP status codes.
- Logs results into `logs/app_health.log`.

**Run:**
```bash
python3 app_health_checker.py
```

---

## ⚙️ Configuration
- Modify `config.json` to adjust thresholds or app URL.
- Example:
```json
{
  "cpu_threshold": 75,
  "memory_threshold": 80,
  "disk_threshold": 90,
  "check_interval": 15,
  "app_url": "http://127.0.0.1:8080"
}
```

---

## 📜 Logs
- System health logs → `logs/system_health.log`
- App health logs → `logs/app_health.log`
