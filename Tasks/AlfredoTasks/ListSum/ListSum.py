#Is the list that will be added
listOfNumbers = [1,2,3,10,100]

print("What would you like the numbers %s to be added by?" % (listOfNumbers))
number = int(raw_input())

print("Number chosen: %s" % (number))
print("Answers:")

answer = 0
for x in listOfNumbers:
	answer = x + number
	print("%s + %s = %s" % (x, number, answer))