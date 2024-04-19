
from pprint import pprint
import os
from dotenv import load_dotenv
import requests
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d0100b546b9f54fde077c31d84b3eaa5/100DaysPythonFlightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": "Bearer " + os.getenv("SHEETY_API_KEY")
        }

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=os.getenv("SHEETY_ENDPOINT"), headers=self.headers)
        data = response.json()
        #pprint(data)
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        print("Updating destination codes...")
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            #response.raise_for_status()
            print(response.text)





