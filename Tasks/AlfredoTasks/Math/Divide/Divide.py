#creates a formula to divide numbers "a" and "b"
print("What number would you like to be divided")
a = int(raw_input())

print("What number would you like %s to be divided by?" % (a))
b = int(raw_input())

def div (a,b):
	c = a/b
	print("%s / %s = %s" % (a,b,c))

print(div(a,b))
