import requests
import json
import datetime
import pandas as pd

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "59e915febd63afee43e6cb4897fc2f6d"

PARAMS = {
    "lat" : 50.45,
    "lon" : 30.52,
    "appid" : API_KEY,
    "cnt" : 5,
    "units" : "metric",
    "lang" : "ua"
}

data = requests.get(URL, params=PARAMS).json()
#with open('weather_Kyiv.json', 'w', encoding="utf-8") as file:
    #json.dump(data , file, indent=5, ensure_ascii=False)

#print(data['list'])

TABLE = []
for day in data['list']:
    ROW = {
        "date" : datetime.datetime.fromtimestamp(day['dt']),
        "main" : day['weather'][0]['main'],
        "temperature" : day['main']['temp'],
        "min_temperature" : day['main']['temp_min'],
        "max_temperature" : day['main']['temp_max'],
        "wind" : day['wind']['speed'],
    }
    TABLE.append(ROW)

DF = pd.DataFrame(TABLE)
#print(DF[["date", "temperature"]])
print(DF[DF["temperature"] < -8])