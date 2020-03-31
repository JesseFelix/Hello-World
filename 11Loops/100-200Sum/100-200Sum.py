print("What's the lowest number you want summed?")
num1 = int(raw_input()) - 1

print("What's the highest number you want summed?")
num2 = int(raw_input())

print("Number Loop:")

while num1 < num2:
	num1 = num1 + 1
	print("%s + %s = %s" % (num1, 1, num1)),