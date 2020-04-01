string = "this is a string that can have letters in it replaced."

print("What letter would you like to have replaced in the string \"%s\"?" % (string))
letter1 = raw_input()

print("What character would you like to replace %s?" % (letter1))
letter2 = raw_input()

stringReplace = string.replace(letter1, letter2)
print(stringReplace)