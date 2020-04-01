print("What's the lowest number you want summed?")
num1 = int(raw_input())

print("What's the highest number you want summed?")
num2 = int(raw_input())

print("Number Loop:")
 
while num1 < num2:
	print("%s + %s = %s\n" % (num1, 1, num1)),
	num1 = num1 + 1