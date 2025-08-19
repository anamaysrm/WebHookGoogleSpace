import requests
import datetime

# Replace this with your webhook URL
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAQAs8uFjnM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4PoS_lxnlUKsxtb9zkmYaOkZkPSo_nGyySK3bYHaK1k"

today = datetime.date(2025, 8, 1)
end_date = datetime.date(2025, 8, 31)

if today <= end_date:
    message = {
  "text": (
    "👟 *Team,* lace up — 15,000 steps/day! \n"
    "💡 Walk during calls, take stairs, keep moving! \n"
    "🏆 *Reward:* ₹1 Lakh* (terms & conditions apply — shake-shake and walk less-less, that’s how you make-make 💰)"
  )
}

    response = requests.post(WEBHOOK_URL, json=message)
    print(f"Status: {response.status_code}, Response: {response.text}")
else:
    print("Walkathon period is over.")
