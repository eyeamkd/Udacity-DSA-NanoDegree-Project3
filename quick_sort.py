from cmath import pi
from os import preadv


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
         
        
    

print( quick_sort([5,6,1,3,2,8,0,4]))     
        