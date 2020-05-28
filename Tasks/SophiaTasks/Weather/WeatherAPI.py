import requests
import json

#prints two questions, in which the answer will decide where the weather report is from
print("What state are you in?")
state = raw_input()
print("What city are you in?")
city = raw_input()

#the url for the request which will have the location inputed
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Hawthorne,California&units=imperial&appid=5923776c853aafa9163de1228843bd76") #% (city, state))

#if "result" is written, it will find the typed info within the .json file
result = response.json()

main = result["main"]
coord = result["coord"]

#code is calling all the info required
if result["cod"] != "404":
  temperature = main["temp"]
  latitude =  coord["lat"]
  longitude = coord["lon"]
  windSpeed = result["wind"]["speed"]

  #Displayes all the info that was requested
  print("The temperature in %s, %s is %s degrees fahrenheit." % (city, state, temperature))
  print("The coordinates of %s, %s is %s, %s" % (city, state, latitude, longitude))
  print("The windspeed in %s, %s is %smph" % (city, state, windSpeed))

#if the location isn't valid
else: 
    print("City not found.") 