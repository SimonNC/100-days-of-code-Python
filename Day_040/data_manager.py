from pprint import pprint
import requests

import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": "Bearer " + os.getenv("SHEETY_API_KEY")
        }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers=self.headers)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
