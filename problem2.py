def rotated_array_search(arr,value)->int: 
    # arr = input[0]
    # value = input[1]
    # pivot_search   
    pivot_index = pivot_search(arr,0,len(arr)-1) 
    #print("Pivot index is", pivot_index)
    if arr[pivot_index] == value:
        return pivot_index
    # print(pivot) 
    if arr[0]<=value<=arr[pivot_index]:
        return binary_search(arr,0,pivot_index,value)
    else:
       return binary_search(arr,pivot_index+1,len(arr)-1, value)
    
    # binary_search on the appropriate half  
    # return target index 
    pass

def binary_search(arr, low, high, value): 
    if low<=high:
        mid = (low+high)//2
        if arr[mid] == value:
            return mid
        else:
            if arr[mid] > value:
                return binary_search(arr,low, mid-1, value)
            else:
                return binary_search(arr, mid+1, high, value)
    return -1
            
    

def pivot_search(arr:list, low, high)->int: 
    if high == low:
        #print("Pivot is", high)
        return high    
    if arr[low] > arr[high]:   
        mid = (low+high)//2   
        if arr[low] >= arr[mid]:
            return pivot_search(arr,low,mid)
        else: 
            return pivot_search(arr,mid,high)
    else:
        return None 


        
# testing  

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) 

#print(rotated_array_search([4,5,6,7,0,1,2],0))
    
    