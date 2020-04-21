#Creates a string that then splits it
print("Type a string you want to split.")
string = raw_input()

def split(string):
	return [char for char in string] 

print(split(string))