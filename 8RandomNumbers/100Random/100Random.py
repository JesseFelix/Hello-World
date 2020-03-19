#generates 100 numbers ranging between 0-100

import random

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 

num = 100
start = 0
end = 100
print(Rand(start, end, num)) 