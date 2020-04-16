#creates a formula to add "a" and "b" numbers
print("What's the first number you would like to add?")
a = int(raw_input())

print("What is the second number you would like to add?")
b= int(raw_input())

def add (a,b):
	c = a+b
	print("%s + %s = %s" % (a,b,c))

print(add(a,b))
