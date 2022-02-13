def maximum_sum_sub_array(arr:list)->int:
    # loop through the array 
    # have a variable sum to calculate sum of each element  
    # check the sum against a "max" variable 
    # if the sum < 0  then, change it back to zero and keep the max intact 
    # repeat this process for every element 
    sum = 0
    max = -999 
    count = 0
    for i in arr:
       temp = sum + i 
       if temp > max:
            max = temp  
       if temp>0:
           sum = temp 
       else: 
           sum = 0 
         
    return max 
                 
    

print(maximum_sum_sub_array([-2, -5, 6, -2, -3, 1, 5, -6]))    