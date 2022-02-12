def pair_sum(arr:list, target:int)->list:  
    # find target sum in the array 
    # sort array and do binary search on the array  
    arr.sort() 
    for element in arr:
        value = target-element  
        index = binary_search(arr,value, 0, len(arr)-1)
        if index: 
            if value< element:
                return [value, element]
            else:
                return [element, value]   
    return [None, None]

def binary_search(arr, element, low, high):   
    while low<=high:
        mid = (low+high)//2 
        if element == arr[mid]:
            return mid
        if element > arr[mid]:
           return binary_search(arr,element,mid+1,high)
        else:
           return binary_search(arr,element,low,mid-1)
    return None 

print(pair_sum([2, 7, 11, 15], 9))