print("Give me a number between 1 and 10:")
number = int(raw_input())

if number > 10 or number < 1:
	print("invalid number")
else:
	print("you chose number " + str(number))
