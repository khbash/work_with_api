import requests

URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "59e915febd63afee43e6cb4897fc2f6d"

PARAMS = {
    "lat" : 50.45,
    "lon" : 30.52,
    "appid" : API_KEY,
    "exclude" : "daily",
    "units" : "metric",
    "lang" : "ua"
}

data = requests.get(URL, params=PARAMS).json()
#print(data.json())



import json
with open('weather_Kyiv.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=5, ensure_ascii=False)

#print(f"мінімальна температура за день: {data['main']['temp_min']}")
#print(f"максимальна температура за день: {data['main']['temp_max']}")
