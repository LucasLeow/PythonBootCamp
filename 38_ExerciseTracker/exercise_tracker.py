import os
import requests
from datetime import datetime

# ================================= Config data =================================
nutri_id = os.environ['nutri_id']
nutri_api_key = os.environ['nutri_api_key']
sheety_api_key = os.environ['sheety_api_key']
sheety_token = os.environ['sheety_token']

nutri_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = f'https://api.sheety.co/{sheety_api_key}/lucasWorkouts/workouts'


# ================================= INFO FROM NUTRI =================================
usr_input = input('Tell me which exercises you did: ')

nutri_exercise_params = {
    "query": usr_input
}

nutri_headers = {
    "Content-Type": "application/json",
    "x-app-id": nutri_id,
    "x-app-key": nutri_api_key
}

nutri_res = requests.post(
    url=nutri_exercise_endpoint,
    json=nutri_exercise_params,
    headers=nutri_headers
)

nutri_data = nutri_res.json()["exercises"][0]

# ================================= POST TO SHEETY =================================
today = datetime.today()

# Fields
todate = today.strftime('%d/%m/%Y')
totime = today.strftime('%H:%M:%S')
exercise = nutri_data["name"]
duration = nutri_data["duration_min"]
calories = nutri_data["nf_calories"]

print(todate, totime, exercise, duration, calories)

sheety_params = {
    "workout": {
        "date": todate,
        "time": totime,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {sheety_token}"
}

sheety_res = requests.post(
    url=sheety_endpoint,
    json=sheety_params,
    headers=sheety_headers
)

print(sheety_res.json())

