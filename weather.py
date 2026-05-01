import requests

def get_location():
    try:
        # uses geolocation to find coords
        response = requests.get('https://geolocation-db.com/json/').json()
        return response['city'], response['latitude'], response['longitude']
    except:
        return "Unknown", None, None
    
def run():
    print("\n--- Local Weather App ---")
    city, lat, lon = get_location()

    if not lat:
        print("Could not dectect location. Please check your internet.")
        return
    
    print(f"Detecting weather for: {city}...")

    # meteo api
    url = f"https://open-meteo.com{lat}&longitude={lon}&current_weather=true"

    try:
        data = requests.get(url).json()
        current = data['current_weather']
        temp = ['temperature']
        wind = current['windspeed']

        print(f"\nLocation: {city}")
        print(f"\nTemperature: {temp}°C")
        print(f"Wind Speed: {wind} km/h")
    
    except Exception as e:
        print(f"Error fetching weather")

    input("\Press Enter to return to Main Menu...")