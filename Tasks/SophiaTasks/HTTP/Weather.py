import requests

print("What state are you in?")
state = raw_input()

print("What city are you in?")
city = raw_input()

#api.openweathermap.org/data/2.5/weather?q=HawthorneCA&appid=5923776c853aafa9163de1228843bd76

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=5923776c853aafa9163de1228843bd76" % (city, state))
print(response)