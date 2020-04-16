import requests
import json

print("What state are you in?")
state = raw_input()

print("What city are you in?")
city = raw_input()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=imperial&appid=5923776c853aafa9163de1228843bd76" % (city, state))

x = response.json()

y = x["main"]

if x["cod"] != "404":

	temperature = y["temp"]

	z = x ["weather"]

	weather_description = z[0]["description"] 
  
    # print following values 
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