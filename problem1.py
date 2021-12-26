def get_square_root(number:int): 
    if(number==1 or number ==0):
        return number
    low = 2
    high = number
    while(low<high):
        mid = (low+high)//2 
        prev_mid = mid-1 
        if(prev_mid*prev_mid< number and mid*mid > number): 
            if((number - prev_mid*prev_mid) < (mid*mid-number)):
                return prev_mid 
            else:
                return mid
        if(mid*mid >= number):
            high = mid
        else:
            low = mid 

print(get_square_root(27))