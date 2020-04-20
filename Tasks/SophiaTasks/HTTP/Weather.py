import requests
import json

print("What state are you in?")
state = raw_input()

print("What city are you in?")
city = raw_input()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=imperial&appid=5923776c853aafa9163de1228843bd76" % (city, state))

result = response.json()

main = result["main"]
coord = result["coord"]

if result["cod"] != "404":
  temperature = main["temp"]
  latitude =  coord["lat"]
  longitude = coord["lon"]

  print("The temperature in %s, %s is %s degrees fahrenheit." % (city, state, temperature))
  print("The coordinates of %s, %s is %s, %s" % (city, state, latitude, longitude))

else: 
    print("City not found.") 