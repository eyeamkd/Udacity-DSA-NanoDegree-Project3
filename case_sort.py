from re import L


def merge(left_arr:list, right_arr:list)->list:
    left_index = 0
    right_index = 0   
    print("left half ", left_arr) 
    print("right arr is", right_arr)
    
    sorted_arr= []
    
    left_index_limit = len(left_arr) - 1
    right_index_limit = len(right_arr) - 1
     
    while left_index <= left_index_limit and right_index <= right_index_limit:
        if(left_arr[left_index]<right_arr[right_index]):
            sorted_arr.append(left_arr[left_index])
            left_index+=1 
        else:
            sorted_arr.append(right_arr[right_index])
            right_index+=1 
    if left_index-1 == left_index_limit:
        while right_index <= right_index_limit:
            sorted_arr.append(right_arr[right_index])
            right_index+=1 
    elif right_index-1 == right_index_limit:
        while left_index <= left_index_limit:
            sorted_arr.append(left_arr[left_index])
            left_index+=1 
    
    print("Sorted array is", sorted_arr)  
            
    return sorted_arr
    
            
def merge_sort(arr:list)->list:
    # recursively divide the array until you reach single element
    # depending on the sorting condition sort the array while merging it back   
    length = len(arr) 
    if length == 1:
        return arr 
    
    else:
        mid = length//2 
        left_half = merge_sort(arr[:mid]) 
        right_half = merge_sort(arr[mid:])  
      
        
        merged_array = merge(left_half,right_half)
        
    return merged_array
    




def case_sort(word:str)->str:
    word_list = [char for char in word] 
    print("Word list is", word_list)
    
    # perform merge sort on the list  
    lower_case_list = []
    upper_case_list = []
    
    for letter in word_list:
        if letter.isupper():
            upper_case_list.append(letter)
        else:
            lower_case_list.append(letter) 
    print(upper_case_list)
    print(lower_case_list)
    upper_case_list = merge_sort(upper_case_list)
    lower_case_list = merge_sort(lower_case_list) 
    
    result = ''
    
    print(upper_case_list)
    print(lower_case_list)
    lower_case_index = 0
    upper_case_index = 0 
    
    for letter in word_list: 
        if letter.isupper(): 
            result+=upper_case_list[upper_case_index]
            upper_case_index+=1 
        else:
            result+=lower_case_list[lower_case_index]
            lower_case_index+=1
            
    
    return result
             
            
print(case_sort('fedRTSersUXJ'))