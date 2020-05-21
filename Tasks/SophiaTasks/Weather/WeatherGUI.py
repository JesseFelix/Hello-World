#//imports new commands
import requests
import json
from Tkinter import *
import tkFont
import tkMessageBox

#//window is referred to as "root"
root = Tk()
root.title("Weather")

#//prints two questions, in which the answer will decide where the weather report is from
stateLabel = Label(root, text = "What state are you in?")
stateLabel.grid(row = 0, column = 0)

stateEntry = Entry(root)
stateEntry.grid(row = 1, column = 0)

cityLabel = Label(root, text = "What city are you in?")
cityLabel.grid(row = 2, column = 0)

cityEntry = Entry(root)
cityEntry.grid(row = 3, column = 0)

#//the url for the request which will have the location inputed

fontStyleLocation = tkFont.Font(family = "Lucida Grande", size = 15)
locationLabel = Label(root, text =" ", font = fontStyleLocation)
locationLabel.grid(row = 0, column = 3)
#Setting up temperature label
degree_sign= u"\N{DEGREE SIGN}" #//Degree symbol
fontStyleTemp = tkFont.Font(family = "Lucida Grande", size = 24) #//Font
#//Actual temperature label
temperatureLabel = Label(root, text = " ", font = fontStyleTemp)
temperatureLabel.grid(row = 1, column = 3)
#//wind label
windLabel = Label(root, text = " ")
windLabel.grid(row = 2, column = 3)
#//coordinates label
coordinatesLabel = Label(root, text = " ")
coordinatesLabel.grid(row = 3, column = 3)

def weather():
	state = stateEntry.get()
	city = cityEntry.get()
#//link with API key
	response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=imperial&appid=5923776c853aafa9163de1228843bd76" % (city, state))
#//if "result" is written, it will find the typed info within the .json file
	result = response.json()
	if result["cod"] != "404":
#//temperature
		main = result["main"]
		temperature = main["temp"]	
#//coordinates
		coord = result["coord"]
 		latitude =  coord["lat"]
 	 	longitude = coord["lon"]
#//wind speed
		windSpeed = result["wind"]["speed"]
#//code is calling all the info required
		fontStyleLocation = tkFont.Font(family = "Lucida Grande", size = 15)
		locationLabel.config(text = "%s, %s" % (city, state), font = fontStyleLocation)
#Setting up temperature label
		degree_sign= u"\N{DEGREE SIGN}" #//Degree symbol
		fontStyleTemp = tkFont.Font(family = "Lucida Grande", size = 24) #//Font
#//Actual temperature label
		temperatureLabel.config(text = "%s %sF" % (temperature, degree_sign), font = fontStyleTemp)
#//wind label
		windLabel.config(text = "Windspeed: %smph" % (windSpeed))
#//coordinates label
		coordinatesLabel.config(text = "Coordinates: %s, %s" % (latitude, longitude))

#//if link does not work
	else:
		locationLabel.config(text = "Location Not Found")
		temperatureLabel.config(text = " ")
		windLabel.config(text = " ")
		coordinatesLabel.config(text = " ")

#How the button works
weatherButton = Button(root, text = "Weather", command = weather)
weatherButton.grid(row = 4, column = 0)

#keeps the window open
root.mainloop()