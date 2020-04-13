print("What year is it?")
year = int(raw_input())

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
	print("Leap year!")
else:
	print("Not a leap year.")