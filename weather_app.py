import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    curr = data['current_condition'][0]
    
    print(f"\n--- Weather for {city.upper()} ---")
    print(f"Temperature: {curr['temp_C']}°C")
    print(f"Condition: {curr['weatherDesc'][0]['value']}")
    print(f"Humidity: {curr['humidity']}%")
    print(f"Wind: {curr['windspeedKmph']} km/h")

city = input("Enter City Name: ")
get_weather(city)
