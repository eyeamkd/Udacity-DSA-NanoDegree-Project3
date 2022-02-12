
def kth_largest(arr:list, k:int)->int:
    # divide the array into groups of five 
    groups = divide_into_five(arr) 
    n = len(arr)
    print(groups)
    # find the median in those groups 
    medians = [group_median(group) for group in groups]
    pivot = kth_largest(medians,n/10) 
    # divide the array into three categories, greater than M, equal to M, less than M 
    arr_less_p = []
    arr_equal_p = []
    arr_greater_p = []
    
    for i in arr:
        if i < pivot:
            arr_less_p.append(i)
        elif i > pivot:
            arr_greater_p.append(i)
        else:
            arr_equal_p.append(i) 
    
    # recurse on the slices to get the final answer
    if k <= len(arr_less_p):
        kth_largest(arr_less_p,k)
    elif k >= len(arr_less_p) + len(arr_equal_p):
        kth_largest(arr_greater_p,k)
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

def group_median(group:list):
    group.sort()
    return group[len(group)//2]

     


kth_largest([6, 80, 36, 8, 23, 7, 10, 12, 42, 99],9)
         