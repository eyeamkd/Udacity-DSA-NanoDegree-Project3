from numpy import left_shift


def merge_sort_divide(arr:list)->list: 
    # divide routine 
    length = len(arr) 
    if(length==1): 
        return arr[0] 
    half_index = length//2 
    left_half =  merge_sort_divide(arr[0:half_index])
    right_half = merge_sort_divide(arr[half_index:]) 
    # sort half routine  
     
    # merge divided half routine  
    return merge_sort(left_half, right_half) 
    pass

def merge_sort(arr1:list,arr2:list)->list:  
    if(arr1[0]>arr2[0]):
        return [arr1[0],arr2[0]]
    else:
        return [arr2[0],arr1[0]]
    
    pass

def merge(arr:list)->list:
    pass 