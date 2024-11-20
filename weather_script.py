##generar código que se conecte a la API de OpenWeatherMap.org y obtenga el clima actual de la ciudad que el usuario ingrese.
import requests
import json
def weather(city):
    api_key = "92d575819c61c039e044b1eea9664027"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))
    else:
        print(" City Not Found ")
city = input("Enter the city name: ")
weather(city)

