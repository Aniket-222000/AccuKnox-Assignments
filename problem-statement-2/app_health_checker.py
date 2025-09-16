#!/usr/bin/env python3
import requests
import logging
import json
import time

with open("config.json") as f:
    config = json.load(f)

APP_URL = config["app_url"]
CHECK_INTERVAL = config["check_interval"]

logging.basicConfig(
    filename="logs/app_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_app():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            msg = f"✅ Application is UP | Status Code: {response.status_code}"
            print(msg)
            logging.info(msg)
        else:
            msg = f"⚠️ Application is DOWN | Status Code: {response.status_code}"
            print(msg)
            logging.error(msg)
    except requests.exceptions.RequestException as e:
        msg = f"❌ Application is DOWN | Error: {e}"
        print(msg)
        logging.error(msg)

if __name__ == "__main__":
    while True:
        check_app()
        time.sleep(CHECK_INTERVAL)
