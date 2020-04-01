#Print the maximum value from listOfNumbers
listOfNumbers = [1,2,3,10,100]

print("Maximum value of %s" % (listOfNumbers))
answer = 0

for item in listOfNumbers:
	if item > answer:
		answer = item 

print("The maximum value is %s" % (answer))