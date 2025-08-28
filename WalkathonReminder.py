import requests
import datetime

# Replace this with your webhook URL
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAQAs8uFjnM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4PoS_lxnlUKsxtb9zkmYaOkZkPSo_nGyySK3bYHaK1k"

today = datetime.date(2025, 8, 1)
end_date = datetime.date(2025, 8, 30)

if today <= end_date:
    message = {
  "text": "😅 Shoes are tired, legs are sore, but hearts are stronger than ever!  \nJust 2 days left — let’s squeeze out those final steps and make the ₹1 Lakh chase worth it. 🏃‍♂️💨  \nEnd strong, laugh louder, walk prouder! 🚀"
}

    response = requests.post(WEBHOOK_URL, json=message)
    print(f"Status: {response.status_code}, Response: {response.text}")
else:
    print("Walkathon period is over.")
