print("Username:")
user = raw_input()
print("Username: " + user)

print("Password: ")
passw= raw_input()

actPassw = "Apple"
if passw == actPassw:
	print("Login Successful")
else:
	print("Incorrect Username or Password")
