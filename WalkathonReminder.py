import requests
import datetime

# Replace this with your webhook URL
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAAAHgOtlvM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=UVDhaEUaIHwaHnWy8IesalKakNQqkYmxgMpuMi4GPyE"

today = datetime.date(2025, 8, 1)
end_date = datetime.date(2025, 8, 31)

if today <= end_date:
    message = {
        "text": (
            "🫡 *Team,* it’s time to *lace up and move!* Every step brings us closer to the top. 👟\n\n"
            "🎯 *Goal:* *10,000 steps per person per day*  \n"
            "💡 *Tip:* Walk during calls, take the stairs, and keep those feet active! 🚶‍♂️🚶‍♀️💨\n\n"
            "📆 *Starts:* August 01, 2025  \n"
            "🏁 *Ends:* August 31, 2025  \n"
            "🥇 *Prize:* Eternal glory (and maybe more 😏)\n\n"
            "🔥 Let's make today count — step strong, step proud! 💪💙"
        )
    }

    response = requests.post(WEBHOOK_URL, json=message)
    print(f"Status: {response.status_code}, Response: {response.text}")
else:
    print("Walkathon period is over.")
