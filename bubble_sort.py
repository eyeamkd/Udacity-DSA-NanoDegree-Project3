from numpy import sort


def bubblesort(arr:list)->list:
    for i in arr:
        for j in arr:
            if i > j:
                temp = i 
                index_i = arr.index(i)
                index_j = arr.index(j)
                arr[index_i] = j
                arr[index_j] = temp
    return arr 

def swap(arr:list, i:int, j:int)->list:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 
    return arr

arr = [ 3, 1, 2, 6, 8, 9, 0, 4] 
sorted_arr = bubblesort(arr)
print(sorted_arr)