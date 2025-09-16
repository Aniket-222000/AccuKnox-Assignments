#!/usr/bin/env python3
import psutil
import logging
import json
import time

with open("config.json") as f:
    config = json.load(f)

CPU_THRESHOLD = config["cpu_threshold"]
MEMORY_THRESHOLD = config["memory_threshold"]
DISK_THRESHOLD = config["disk_threshold"]
CHECK_INTERVAL = config["check_interval"]

logging.basicConfig(
    filename="logs/system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def monitor_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    alerts = []

    if cpu > CPU_THRESHOLD:
        alerts.append(f"⚠️ High CPU usage: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"⚠️ High Memory usage: {memory}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"⚠️ Low Disk Space: {disk}% used")

    if alerts:
        for alert in alerts:
            print(alert)
            logging.warning(alert)
    else:
        msg = f"✅ System Healthy | CPU: {cpu}% | MEM: {memory}% | DISK: {disk}%"
        print(msg)
        logging.info(msg)

if __name__ == "__main__":
    while True:
        monitor_system()
        time.sleep(CHECK_INTERVAL)
