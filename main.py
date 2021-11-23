import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = input("Enter your Nutritionix API ID: ")
APP_KEY = input("Enter your Nutritionix API KEY: ")
SHEETY_API_KEY = input("Enter your SHEETY API KEY: ")


SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/workoutTracker/workouts"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("What exercises did you do: ")

exercise_params = {
 "query":query,
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=header)
processedExercise = exercise.json()
print(processedExercise)

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")


for exercise in processedExercise['exercises']:
    sheet_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "calories": exercise["nf_calories"],
            "duration": exercise["duration_min"]
    }}

    newRow = requests.post(url=SHEETY_ENDPOINT, json=sheet_params, auth=HTTPBasicAuth('panam-py', 'ihatebarca10'))
    print(newRow.text)
