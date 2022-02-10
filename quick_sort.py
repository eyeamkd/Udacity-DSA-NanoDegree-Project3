from urllib3 import Retry


def quick_sort(arr:list)->list: 
    if len(arr) <= 1:
        return arr 
    else: 
        pivot = arr[-1]
        left_half = []
        right_half = []
        for element in arr[:-1]:
            if element < pivot:
                left_half.append(element)
            else:
                right_half.append(element)
        sorted_left_half = quick_sort(left_half)
        sorted_right_half = quick_sort(right_half)    
    return sorted_left_half + [pivot] + sorted_right_half 

def in_place_sort(arr:list, pivot_index:int, element_index:int)->list: 
     
    if pivot_index > 0:
        prev_index = pivot_index - 1
        temp = arr[prev_index]
        arr[prev_index] = arr[pivot_index]
        arr[pivot_index] = arr[element_index]
        arr[element_index] = temp 
        pivot_index = prev_index 
    
    return arr, pivot_index
         
        
def quick_sort_in_place(arr:list)->list:
    if len(arr) > 2:
        pivot_index = len(arr) -1  
        element_index = 0
        while pivot_index > element_index:
            if arr[element_index] > arr[pivot_index]: 
                if(len(arr)>3): 
                    prev_index = pivot_index - 1
                    temp = arr[prev_index] 
                    pivot = arr[pivot_index]
                    element = arr[element_index]
                    arr[prev_index] = pivot
                    arr[pivot_index] = element
                    arr[element_index] = temp 
                    pivot_index -=1  
                else:
                    pivot = arr[pivot_index]
                    element = arr[element_index] 
                    arr[pivot_index] = element
                    arr[element_index] = pivot 
                    pivot_index-=1
            else:
                 element_index+=1
                # arr, pivot_index = in_place_sort(arr, pivot_index, element_index) 
        
        sorted_left_half = quick_sort_in_place(arr[:pivot_index])
        sorted_right_half = quick_sort_in_place(arr[pivot_index+1:])
        return sorted_left_half+[arr[pivot_index]]+sorted_right_half 
    elif len(arr)==2:
        if arr[0]>arr[1]: 
            new_arr = [arr[1], arr[2]]
            return new_arr
    else:
        return arr    

print( quick_sort_in_place([5,6,1,3,2,8,0,4]))     
        