def get_min_max(input:list): 
    max = -9999 
    min = 100000 
    min_sum = 0
    max_sum = 0 
    
    for i in input:
        if i < min:
            min = i
        if i > max:
            max = i 
            
    return (min,max)
            
        
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")