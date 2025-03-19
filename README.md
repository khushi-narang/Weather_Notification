# Weather_Notification

<video src='https://github.com/khushi-narang/Weather_Notification/blob/main/Recording%202025-03-19%20095258.mp4' width=180/>
### Requirements
Installation of pywin32

### Steps to Use:
1. Install the required libraries:
   
```
 pip install win10toast requests
```
If it causes issues try:
   
```
 pip install win10toast-persist requests
```
or 
   
```
 pip install pywin32
 pip install win10toast-persist requests
```

2. Run the script to get a weather notification.

### Note
- Replace API_KEY = "" with a real API key from OpenWeatherMap. (make sure it's a string)
- Enter your preferred city.
- Runs on Windows and shows a weather notification.

### Getting API key from OpenWeatherMap
1. Sign Up on OpenWeatherMap 
- Go to OpenWeatherMap: [https://openweathermap.org/current](url)
- Create a free account by providing your email and password.
- Verify your email and log in.
2. Get Your API Key
- After logging in, go to your API keys section: [https://home.openweathermap.org/api_keys](url)
- You will see a default key named something like "default" under "API keys."
- If you don’t see one, click "Create Key" and give it a name (e.g., "MyWeatherApp"), and save.

### Documentation of OpenWeatherMap Current Weather
[https://openweathermap.org/current](url)
### Win10Toast
[https://pypi.org/project/win10toast/](url)
