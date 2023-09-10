import requests
import json

# Get API key
api_key = "f9da77fb42003d7b660905e953289514"

# Get city name
print("|---------------------------------|")
print("|------ Weather Application ------|")
print("|---------------------------------|")
print("Created by:")
print("-> Pratyush Nirwan ")
print("-> Kaustubh Tembhe ")

using = True

while using:
    city = input("Enter the name of the city: ")

    # Make API request
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
    response = requests.get(url)

    # Parse JSON data
    data = json.loads(response.text)

    name= data["name"]

    # Get current temperature
    temp = data["main"]["temp"]

    # Get weather description
    description = data["weather"][0]["description"]

    # Get humidity
    humidity = data["main"]["humidity"]

    # Get wind speed
    wind_speed = data["wind"]["speed"]

    # Get pressure
    pressure = data["main"]["pressure"]

    #set emoji for temprature
    tempEmo = ""
    if temp >= 25:
        tempEmo='☀️';
    elif temp<25 and temp>0:
        tempEmo='☁️'
    elif temp<0:
        tempEmo='❄️'

    #set emoji for weather
    weatherEmo = ""
    if "rain" in description:
        weatherEmo='☔'
    elif "haze" in description:
        weatherEmo='🌫️'
    elif "snow" in description:
        weatherEmo='☃️'
    elif "clear" in description:
        weatherEmo='😎' 
    elif "clouds" or "cloud" in description:
        weatherEmo='☁️'         


    # Print weather data
    print("-----------------------------------")
    print("Weather for {}\n".format(name))
    print("Temperature:{}  {}°C".format(tempEmo, temp))
    print("Weather:{}  {}".format(weatherEmo, description))
    print("Humidity:💦 {}%".format(humidity))
    print("Wind Speed:💨 {} m/s".format(wind_speed))
    print("Pressure:🌪️  {} hPa".format(pressure))
    print("-----------------------------------")

    cnt = input("Want to search again?: ")
    
    if cnt =="n" or cnt=="N":
        using=False