#Multiplication table 1-10

table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("On a table of 1-10 what number do you want multiplied?")
number = int(raw_input())

for x in table:
	result = number * x
	print("%s * %s = %s" % (number, x, result))