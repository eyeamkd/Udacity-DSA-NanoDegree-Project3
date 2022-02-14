def sqrt(number:int): 
    if( type(number) is not int): 
        raise ValueError("Only integer input supported") 
    if(number==1 or number ==0):
        return number
    low = 2
    high = number 
    return binary_search(low, high, number)


def binary_search(low, high,value): 
    if low==high:
        return low  
    mid = (low+high )//2 
    if mid*mid == value:
        return mid 
    if (mid-1)*(mid-1) < value:
        if (mid+1)*(mid+1)>value:
            return mid  
    if mid*mid > value:
      return binary_search(low, mid, value)
    elif mid*mid < value:
        return binary_search(mid, high, value)
    
    return -1
        

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail") 

# print(binary_search(2,16,16))