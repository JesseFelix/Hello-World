#powers of 2
n = 4

x = int(raw_input())

while x < n:
	saveValue = x
	x = x * 2	
	print("%s^2 = %s" % (saveValue, x))
