#has the user type a number between 1-10
print("Give me a number between 1 and 10:")
number = int(raw_input())

#determines if the number is valid. If it is then it prints the number
if number > 10 or number < 1:
	print("invalid number")
else:
	print("you chose number " + str(number))
