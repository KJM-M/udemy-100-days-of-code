import os
import requests
import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

SHEETY_BASIC_AUTH = os.environ.get("SHEETY_BASIC_AUTH")

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_headers = {
    "Authorization": SHEETY_BASIC_AUTH
}

# ----------------------------------- NUTRITION -----------------------------------
nutrition_get_endpoint = "https://app.100daysofpython.dev/healthz"
nutrition_post_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_done = {
    "query": "ran for 45 minutes"
}

nutrition_response = requests.post(nutrition_post_endpoint, json=exercise_done, headers=nutrition_headers)
exercise_data = nutrition_response.json()

exercise = exercise_data["exercises"][0]

exercise_type = exercise["name"]
exercise_duration = exercise["duration_min"]
exercise_calories_burned = exercise["nf_calories"]

# ----------------------------------- SHEETY -----------------------------------

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

today = datetime.date.today().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")

workout = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise_type,
        "duration": exercise_duration,
        "calories": exercise_calories_burned,
    }
}

response = requests.post(sheety_endpoint, json=workout, headers=sheety_headers)
print(response.json())
print(response.status_code)
