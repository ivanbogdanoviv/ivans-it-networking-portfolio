import json
import os
import time
import logging
import getpass
from datetime import datetime
from netmiko import ConnectHandler


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
SAMPLE_DATA_DIR = os.path.join(PROJECT_DIR, "sample-data")

LOG_DIR = os.path.join(PROJECT_DIR, "runtime_logs")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "runtime_outputs")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "automation.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def load_devices(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_output(device_name: str, content: str) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{device_name}_{ts}.txt".replace(" ", "_")
    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    return out_path


def main() -> None:
    devices_path = os.path.join(SAMPLE_DATA_DIR, "devices.json")

    logging.info("Starting show-command automation run")
    logging.info("Loading inventory: %s", devices_path)

    try:
        devices = load_devices(devices_path)
    except Exception as e:
        logging.error("Failed to load devices.json: %s", e)
        return

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    show_commands = [
        "show ip interface brief",
        "
