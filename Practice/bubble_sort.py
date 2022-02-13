from numpy import sort


def bubblesort(arr:list)->list:
    for i in arr:
        for j in arr:
            if i > j and arr.index(i) < arr.index(j):
                temp = i 
                index_i = arr.index(i)
                index_j = arr.index(j)
                arr[index_i] = j
                arr[index_j] = temp
                print(arr)
    return arr 

def swap(arr:list, i:int, j:int)->list:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 
    return arr

arr = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
sorted_arr = bubblesort(arr)
print(sorted_arr) 

sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)] 

def compare_time(time1,time2):
     if time1[0]>time2[0]:
         return True 
     elif time1[0] == time2[0]:
         if time1[1]>time2[1]:
             return True 
     else:
         return False

def bubble_sort_2(arr:list)->list:
    for time1 in arr:
        for time2 in arr:
            time1_index = arr.index(time1)
            time2_index = arr.index(time2) 
            if (compare_time(time1,time2) and time1_index < time2_index) or (not compare_time(time1,time2) and time2_index < time1_index) : 
                temp_time = arr[time1_index]
                arr[time1_index] = arr[time2_index]
                arr[time2_index] = temp_time
            print(arr) 
    return arr 

print(bubble_sort_2(sleep_times))
                
                