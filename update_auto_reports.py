import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Slack Incoming Webhook URL
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


# Slack channel is defined in webhook settings (cannot be overridden in some workspaces)

tasks = [
    {
        "sheet": "<https://docs.google.com/spreadsheets/d/1j90OuslWH3S-oyA75T6DHvbnM3YzcN6Ju80Pm1z7DvM|Tracker_Customer_Support_Inbound_Knowlarity>",
        "message": "Please update the *date range formula of all reports* to ensure the latest data is reflected."
    },
    {
        "sheet": "<https://docs.google.com/spreadsheets/d/1zd3xzmo28v-v3QYxrcrGvnc1IJRlAtoRo2g0pJ5VU-s| MoM/Visits Tracker - Quarter 3 (2025)-(Oct - Dec)> & <https://docs.google.com/spreadsheets/d/12J1FgbWWWiIvbVwHVti9wBMifvJwcEVHtHuzt7USuLo|(Visit form – Responses)>",
        "message": "Stop report on the *last day of the month* and update the *date range accordingly* for the new reporting cycle."
    },
    {
        "sheet": "<https://docs.google.com/spreadsheets/d/1zOPDT5LbULtDTfVYbhFeZ6Wq_BGDFqaUNwmEwHvL72Q| Lead Generation Summary – Inbound & Outbound>",
        "message": "Please verify that *table formatting is intact* and update *date ranges* wherever applicable."
    },
    {
        "sheet": "<https://docs.google.com/spreadsheets/d/19WZWjKdHi3MIvxtQlzPCMMYS8BQg_hgETcoSUxXUhhI| Advance Collection Tracker>",
        "message": "Stop report on the *last day of the month* and update the *date range accordingly*."
    }
]

def send_slack_reminder():
    header = "*🔔 Data Source Update Reminder*\n\n"
    body = ""

    for idx, task in enumerate(tasks, start=1):
        body += (
            f"*{idx}️⃣ {task['sheet']}*\n"
            f"👉 {task['message']}\n\n"
        )

    payload = {
        "text": header + body
    }

    response = requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        print("✅ Reminder sent successfully via webhook")
    else:
        print(f"❌ Failed to send reminder: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_slack_reminder()
