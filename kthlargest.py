
def kth_largest(arr:list, k:int)->int: 
    #base case for the recursion 
    pivot = fast_select(arr) 
    # divide the array into three categories, greater than M, equal to M, less than M 
    arr_less_p = []
    arr_equal_p = []
    arr_greater_p = []
    #print("Pivot is", pivot)
    for i in arr:
        if i < pivot:
            arr_less_p.append(i)
        elif i > pivot:
            arr_greater_p.append(i)
        else:
            arr_equal_p.append(i) 
    
    # recurse on the slices to get the final answer
    if k <= len(arr_less_p):
       return kth_largest(arr_less_p,k)
    elif k > len(arr_less_p) + len(arr_equal_p):
       return kth_largest(arr_greater_p,k - len(arr_less_p) - len(arr_equal_p) )
    else:
        return pivot
    
    
    
    
    
def divide_into_five(arr:list)->list:
    groups = [] 
    count = 0
    slice = []
    for i in range(len(arr)):
        slice.append(arr[i])
        count+=1
        if count == 5:
            groups.append(slice)
            slice = [] 
            count = 0 
    if len(slice) > 0: #accounting for the remaining values in the array
        groups.append(slice) 
    return groups 

def group_median(groups:list): 
    medians = [] 
    for group in groups:
        group.sort()
        medians.append(group[len(group)//2]) 
    return medians 

def fast_select(arr:list):
    if len(arr)==1:
        return arr[0] 
    groups = divide_into_five(arr)
    medians = group_median(groups) 
    return fast_select(medians)
        

     


print(kth_largest([6, 80, 36, 8, 23, 7, 10, 12, 42],5))
         