import requests
from win10toast_persist import ToastNotifier

def get_weather(city="Greater Noida"):
    API_KEY = "" #enter your API key from OpenWeatherMap
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(URL)
        data = response.json()
        
        if data["cod"] == 200:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            return f"{city} Weather: {weather}, {temp}°C"
        else:
            return f"Error: {data.get('message', 'City not found!')}"
    except Exception as e:
        return f"Error: {str(e)}"

def notify_weather():
    toaster = ToastNotifier()
    weather_info = get_weather(input("Enter city: "))
    toaster.show_toast("Weather Update", weather_info, duration=10)

if __name__ == "__main__":
    notify_weather()
