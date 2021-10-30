import requests
import json
url = 'http://api.weatherapi.com/v1/current.json'
params = {"key": "4bbb6a9116034b188e624454213010","q": "New York","aqi":"no"}
response = requests.get(url=url, params=params).text
json_acceptable_string = response.replace("'", "\"")
d = json.loads(json_acceptable_string)
print(d["current"]["humidity"])