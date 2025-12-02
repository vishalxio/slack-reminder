import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def send_slack_message(message: str):
    payload = {"text": message}

    requests.post(
        SLACK_WEBHOOK_URL,
        json=payload
    )

def run_reminder():
    message = """
🔔 *Reminder*

Update CS Snapshot & CS Home:
Paste ARR sheet data into *Email Outstanding* and *Outstanding* tabs.
"""
    send_slack_message(message)

if __name__ == "__main__":
    run_reminder()
