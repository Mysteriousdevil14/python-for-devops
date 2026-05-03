import requests
import json

API_KEY = "82dab9613b4251df5bd94647f4d964c0"

api_url = "http://api.weatherstack.com/"
location = input("Please enter the city name to fetch the weather: ")

query = f'current?access_key={API_KEY}&query={location}'
response = requests.get(url=api_url+query)
# print(response.json())
result = response.json()
location = result["location"]

print(f'Location: {location["name"]},{location["region"]} {location["country"]}  Date&Time: {location["localtime"]}')
print(f'Temperature in {location["name"]} is {result["current"]["temperature"]}°C')
print(f'Currently {result["current"]["weather_descriptions"][0]}')

with open("weather_data.json", "w+") as file:
    json.dump(result, file, indent=4)