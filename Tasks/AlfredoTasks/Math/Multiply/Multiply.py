#creates a formula to multiply "a" and "b"
print("What's the first you number would like to multipled?")
a = int(raw_input())
 
print("What would you like %s to be multipled with?" % (a))
b = int(raw_input())

def mult (a,b):
	c = a * b
	print("%s x %s = %s" % (a,b,c))

print(mult(a,b))
