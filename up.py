import requests
import json


url1= 'http://api.weatherapi.com/v1/current.json?key=ed0deb94339846afb2694943230809&q= '+input("Dear user enter city name-:")

df = requests.get(url1)
data = json.loads(df.content)

print (f"Temperature of {data['location']['name']}is {data['current']}")

