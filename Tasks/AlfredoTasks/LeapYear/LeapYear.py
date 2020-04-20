#Asks the user for the year
print("What year is it?")
year = int(raw_input())

#Does formula to determine if it is a leap year or not
#The perameters are every 4 years is a leap year except every hundred unless that hundred year is divisible by 400
if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
	print("Leap year!")
else:
	print("Not a leap year.")