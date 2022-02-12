from calendar import c


def sort_012(arr:list)->list:
    zero_pointer = 0
    two_pointer = len(arr)-1 
    current_pointer = 0 
    
    while(arr[two_pointer]==2):
        two_pointer-=1  
    while(arr[zero_pointer]==0):
        zero_pointer+=1 
         
    current_pointer = zero_pointer
        
    def swap(index_1, index_2):
        temp = arr[index_1]
        arr[index_1] = arr[index_2]
        arr[index_2] = temp 
    
    while current_pointer <= two_pointer:
        if arr[current_pointer] == 1:
            pass
        elif arr[current_pointer] == 0: 
            if current_pointer != zero_pointer:
                swap(current_pointer,zero_pointer)
                zero_pointer+=1 
                current_pointer-=1
        else: 
            if current_pointer != two_pointer: 
                swap(current_pointer,two_pointer)
                two_pointer-=1
                current_pointer-=1 
        current_pointer+=1  
    return arr 

print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))