print("Would you like to a - Add, b - Subtract, c - Multiply or d - Divide")
ans = raw_input()

#adds two numbers inputed
if ans == "a":
	print("What is the first number you would like to add?")
	aNum1 = int(raw_input())
	print("What is the second number you would like to add?")
	aNum2 = int(raw_input())
	def add(aNum1, aNum2):
		aNum3 = aNum1 + aNum2
		print("%s + %s = %s" % (aNum1, aNum2, aNum3))

	print(add(aNum1, aNum2))

#subtracts two numbers inputed
if ans == "b":
	print("What is the first number would you like to subtract?")
	bNum1 = int(raw_input())
	print("What is the second number you would like to subtract?")
	bNum2 = int(raw_input())
	def sub(bNum1, bNum2):
		bNum3 = bNum1 - bNum2
		print("%s - %s = %s" % (bNum1,bNum2, bNum3))
	print(sub(bNum1, bNum2))

#multiplies two numbers inputed
if ans == "c":
	print("What is the first number you would like to multiply?")
	cNum1 = int(raw_input())
	print("What is the second number you would like to multiply?")
	cNum2 = int(raw_input())
	def mult(cNum1,cNum2):
		cNum3 = cNum1 * cNum2
		print("%s x %s = %s" % (cNum1, cNum2,cNum3))

	print(mult(cNum1,cNum2))

#divides two numbers inputed
if ans == "d":
	print("What is the first number you would like to divide?")
	dNum1 = int(raw_input())
	print("What is the second number you would like to divide?")
	dNum2 = int(raw_input())
	def div(dNum1, dNum2):
		dNum3 = dNum1 / dNum2
		print("%s/%s = %s" % (dNum1, dNum2,dNum3))
	print(div(dNum1, dNum2))