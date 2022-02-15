def get_min_max(input:list):  
    if type(input) is list:
        max = -9999 
        min = 100000 
        
        for i in input: 
            if i is not None:
                if i < min:
                    min = i
                if i > max:
                    max = i
            else:
                raise ValueError("Invalid Input") 
                
        return (min,max) 
    else:
        raise ValueError("Invalid Input")
            
        
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") 
#edge cases
get_min_max([1,2,None, 4])
get_min_max([]) 
print(get_min_max([1,1,1,1,1,1,1]))
