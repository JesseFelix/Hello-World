import requests
import json
from Tkinter import *
import Tkinter as tk
from urllib2 import urlopen
from PIL import ImageTk,Image  
import io
import tkFont

#//is the window that will be created
window = Tk()

window.title("Movie List")

#//scrollBar still WIP
scrollBar = Scrollbar(window)
scrollBar.pack(side = RIGHT, fill = "y")#grid(row = 1, column = 3)


#//the url required for the API
movieList = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=a5f742b557bc804d7687bb27d931810a&language=en-US&page=1")

movie = movieList.json()
results = movie["results"] #Array
for outcome in results:

#//the different calls for the information from the .json file
	title = outcome["title"]
	popularity = outcome["popularity"]
	date = outcome["release_date"]
	poster = outcome ["poster_path"]
	overview = outcome["overview"]

#//The poster setup
	posterURL = urlopen("https://image.tmdb.org/t/p/w300/%s" % (poster)) #//Ad Astra: /xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg"
	posterFull = io.BytesIO(posterURL.read())
	posterShow = Image.open(posterFull)
	posterImage = ImageTk.PhotoImage(posterShow)

#//displays poster
	posterLabel = Label(window, image = posterImage)
	posterLabel.image = posterImage
	posterLabel.pack()

#//creates a label for the title
	titleText = title
	fontStyleTitle = tkFont.Font(family = "Lucida Grande", size = 18)
	titleLabel = Label(window, text = "\n" + titleText, font = fontStyleTitle)
	titleLabel.pack()

#//creates a label for the popularity
	fontStylePandD = tkFont.Font(family = "Lucida Grande", size = 12, weight = "bold")
	dateText = "Release date: %s" % (date)
	popularityText = "Popularity score: %s" % (popularity)
	popularAndDateLabel = Label(window, text = popularityText + "  " + dateText, font = fontStylePandD)
	popularAndDateLabel.pack()

	overviewLabel = Label(window, text = "     " + overview + "\n\n", wraplength = 400, justify = LEFT)
	overviewLabel.pack()

#//keeps window open until manually closed
window.mainloop()