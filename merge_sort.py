def merge_sort_divide(arr: list) -> list:
    # divide routine 
    length = len(arr)
    if length == 1:
        return arr
    half_index = length // 2
    sorted_left_half = merge_sort_divide(arr[:half_index])
    sorted_right_half = merge_sort_divide(arr[half_index:])

    # merge divided half routine  
    return merge(sorted_left_half, sorted_right_half)


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
            merged_array.append(arr1[0])
            arr1.remove(arr1[0])
        else:
            merged_array.append(arr2[0])
            arr2.remove(arr2[0])


# test case for the merge
result = merge_sort_divide([3, 6, 9, 1, 2, 4])
print(result)
