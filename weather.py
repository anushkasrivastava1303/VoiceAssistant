import requests


api_address='http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=1c18161ae5cc9c1f14c64ed3bce754d2'
json_data = requests.get(api_address).json()

def temp():
    temprature = round(json_data["main"]["temp"]-273,1)
    return temprature

def des():
    description = json_data["weather"][0]["description"]
    return description

