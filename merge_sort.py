def merge_sort_divide(arr: list, pairs) -> list:
    # divide routine  
    length = len(arr)
    if length == 1:
        return arr,0
    half_index = length // 2
    sorted_left_half, left_half_pairs = merge_sort_divide(arr[:half_index], pairs)
    sorted_right_half, right_half_pairs = merge_sort_divide(arr[half_index:], pairs)

    # merge divided half routine    
    
    
    merged_array, merged_pairs   = index_merge(sorted_left_half, sorted_right_half,0,0,pairs)  
    
    pairs = max(pairs, merged_pairs)
    
    return merged_array, pairs


def copy_arr(source: list, destination: list) -> list:
    for element in source:
        destination.append(element)
    return destination


def merge(arr1: list, arr2: list) -> list:
    merged_array = []
    while len(arr1) != 0 or len(arr2) != 0:
        if len(arr1) == 0:
            merged_array = copy_arr(arr2, merged_array)
            return merged_array
        elif len(arr2) == 0:
            merged_array = copy_arr(arr1, merged_array)
            return merged_array
        elif arr1[0] < arr2[0]: 
            print("Count here")
            merged_array.append(arr1[0])
            arr1.remove(arr1[0])
        else: 
            print("Count here")
            merged_array.append(arr2[0])
            arr2.remove(arr2[0]) 

def index_merge(arr1:list, arr2:list, arr1_index:int, arr2_index:int, pairs=0)-> list:
    merged_array = [] 
    arr1_length = len(arr1)
    arr2_length = len(arr2)  
    arr1_index_limit = arr1_length - 1
    arr2_index_limit = arr2_length - 1
    while arr1_index <= arr1_index_limit and arr2_index<= arr2_index_limit: 
        print("Array and index are", arr2)
        if(arr1[arr1_index]>arr2[arr2_index]): 
            print("Greater values are ", arr1, arr2)
            pairs+= len(arr1)-arr1_index+1 
            print("Pairs is ", pairs)
            merged_array.append(arr2[arr2_index]) 
            arr2_index+=1 
        else:
            merged_array.append(arr1[arr1_index])
            arr1_index+=1 
    if(arr1_index == arr1_index_limit):
        while arr1_index <= arr1_index_limit:
            merged_array.append(arr1[arr1_index])
            arr1_index+=1
    else:
        while arr2_index <= arr2_index_limit:
            merged_array.append(arr2[arr2_index])
            arr2_index+=1
             
    return  merged_array,pairs  
    
         
            
        
    


# test case for the merge
result, pairs  = merge_sort_divide([7, 5, 3, 1],0)
print("Pairs are ", pairs)
