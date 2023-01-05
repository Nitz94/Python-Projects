import requests
from datetime import datetime

APP_ID = "api id"
API_KEY = "key"
GENDER = "male"
AGE = 28
HEIGHT = 170.10
WEIGHT = 70

exercise_query = input("How much did you work out today? ")

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com"
sheet_endpoint = "https://api.sheety.co/"


nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

tracking_config = {

 "query": exercise_query,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url=nutritionix_exercise_endpoint, json=tracking_config, headers=nutri_headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }


sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, auth=("NithinNazar", "bgFTghju765rft6GH"))
print(sheet_response)

