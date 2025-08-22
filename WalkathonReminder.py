import requests
import datetime

# Replace this with your webhook URL
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAQAs8uFjnM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4PoS_lxnlUKsxtb9zkmYaOkZkPSo_nGyySK3bYHaK1k"

today = datetime.date(2025, 8, 1)
end_date = datetime.date(2025, 8, 31)

if today <= end_date:
    message = {
  "text": "🔥 Only 10 days remain!  \nConsistency beats excuses — every step counts. 🙌  \nLet’s push to 15k daily and rise back in rank!  \n🏆 Reward: ₹1 Lakh — let’s make it ours. 🚀"
}

    response = requests.post(WEBHOOK_URL, json=message)
    print(f"Status: {response.status_code}, Response: {response.text}")
else:
    print("Walkathon period is over.")
