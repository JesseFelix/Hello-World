#printing a string of numbers
array = [1,2,3,4,5,6,7]

array.insert(3,19)
array.insert(7,8)

array.remove(2)
array.remove(5)

array.append(9)
array.append(10)

array.pop()
array.pop()

print("The array is %s" %(array))

length = len(array)

print("There are %s characters in the array." % (length))