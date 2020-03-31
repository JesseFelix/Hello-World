mylist = [1, 2, 3, 4, 5]

print("What number would you like the table to be added with?")
num= int(raw_input())

for x in mylist:
	ans = num + x
	print("%s + %s = %s" % (num, x, ans))