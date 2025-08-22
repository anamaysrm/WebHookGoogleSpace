import requests
import datetime

# Replace this with your webhook URL
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAQAs8uFjnM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4PoS_lxnlUKsxtb9zkmYaOkZkPSo_nGyySK3bYHaK1k"

today = datetime.date(2025, 8, 1)
end_date = datetime.date(2025, 8, 31)

if today <= end_date:
    message = {
  "text": "🔥 Just 10 days left!  \nRajesh shows us that consistency beats excuses — 10k every single day. 🙌  \nConsistency like Rajesh’s is the secret sauce — add some extra steps and we’ve got victory! ✨  \n🏆 Reward: ₹1 Lakh — let’s make it ours. 🚀"
}

    response = requests.post(WEBHOOK_URL, json=message)
    print(f"Status: {response.status_code}, Response: {response.text}")
else:
    print("Walkathon period is over.")
