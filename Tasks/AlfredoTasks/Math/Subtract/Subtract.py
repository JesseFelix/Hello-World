#creates a formula to subtract "a" and "b"

#asks the user if they want their answer to always be positive
print("Would you like the answer to always be positive? (yes/no)")
answer = raw_input()

#has the user decide what "a" equals
print("What's the first number you would like to have subtracted?")
a = int(raw_input())

#has the user decide what "b" equals
print("What's the second number you would like to have subtracted?")
b = int(raw_input())


if answer == "yes":
	#the formula for if the user wants the answer to always be positive
	def sub (a,b):
		c = a - b
		if c > 0:
			print("%s - %s = %s" % (a,b,c))
			print("originally positive")
		else:
			d = b - a
			print("%s - %s = %s" % (b,a,d))
			print("originally negative")
	print(sub(a,b))

if answer == "no":
	c = a - b
	print("%s - %s = %s" % (a, b, c))


