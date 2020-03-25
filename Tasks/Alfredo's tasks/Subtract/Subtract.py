#creates a formula to add "a" and "b" numbers
#outcome will only be positive

a=6
b=30

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
