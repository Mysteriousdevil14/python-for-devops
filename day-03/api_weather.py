import requests
import json

API_KEY = "82dab9613b4251df5bd94647f4d964c0"

api_url = "http://api.weatherstack.com/current"

def fetch_weather_data(location):
    try:
        query = f'?access_key={API_KEY}&query={location}'
        response = requests.get(url=api_url+query)
        # print(response.json())
        result = response.json()
        if "error" in result:
            error_info = result["error"]

            if error_info.get("code") == 104:
                print("API limit reached. Please upgrade your plan.")
            elif error_info.get("code") == 615:
                print("Invalid location. Please check the city name.")
            else:
                print(f"API Error: {error_info.get('info', 'Unknown error')}")
            return

        location = result["location"]

        print(f'Location: {location["name"]},{location["region"]} {location["country"]}  Date&Time: {location["localtime"]}')
        print(f'Temperature in {location["name"]} is {result["current"]["temperature"]}°C')
        print(f'Currently {result["current"]["weather_descriptions"][0]}')

        with open("weather_data.json", "w+") as file:
            json.dump(result, file, indent=4)
    
    except KeyError as error:
        print(f'Missing expected data in response: {error}')


location = input("Please enter the city name to fetch the weather: ")
fetch_weather_data(location)