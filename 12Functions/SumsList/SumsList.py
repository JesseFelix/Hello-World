#shows the list
mylist = [1, 2, 3, 4, 5]

#has the user decide what to multiply the list by
print("What number would you like the table to be added with?")
num= int(raw_input())

#multiplies the list with whatever the inputed number is
for x in mylist:
	ans = num + x
	print("%s + %s = %s" % (num, x, ans))