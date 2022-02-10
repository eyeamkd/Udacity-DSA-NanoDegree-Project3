def count_inversion_pairs(arr:list)->int:
    # divide the array into two halves 
    
      pass 

def divide_array(arr:list):
    length = len(arr) 
    if length == 1:
        return arr 
    mid = length//2 
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    merged_array = merge(left_half,right_half)
     

def merge(left_half:list,right_half:list)->list:
    pass
    
    
    
    # while merging the left and the right half apply the logic 
    