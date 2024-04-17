import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

nutritionix_api_key = os.getenv("API_KEY")
nutritionix_app_id = os.getenv("APP_ID")
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

host_domain = "https://trackapi.nutritionix.com"
NL_ENDPOINT = "/v2/natural/exercise"
request_url = f"{host_domain}{NL_ENDPOINT}"
exercice_text = input("Tell me which exercice you want to track: ")

sheet_endpoint = os.getenv("SHETTY_ENDPOINT")

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key
}

parameters = {
    "query": exercice_text,
    "gender": "male",
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(request_url, headers=headers, json=parameters)
result = response.json()

headers = {
    "Authorization": "Bearer Hello123"
}

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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)
