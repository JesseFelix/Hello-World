#asks the user for a username
print("Username:")
user = raw_input()
print("Username: " + user)

#asks the user for a password
print("Password: ")
password= raw_input()

#shows what the password
currentPassword = "Apple"

#checks if the password typed is the same as the current password
if password == currentPassword:
	print("Login Successful")
else:
	print("Incorrect Username or Password")
