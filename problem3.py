from numpy import number
from Practice.quick_sort import quick_sort_in_place


def rearrange_digits(input_list): 
    if len(input_list)>0 and type(input_list) is not list:
        sorted_list = quick_sort_in_place(input_list)
        number1=''
        number2='' 
        for i in sorted_list[::-1]: 
            if type(i) is not None:
                if i%2==0:
                    number1+=str(i) 
                else:
                    number2+=str(i) 
            else:
                raise ValueError("Invalid Input") 
        return [int(number1), int(number2)] 
    else:
        raise ValueError("Invalid Input")

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]]) 
#edge cases
test_function([[], [542, 31]])
test_function([[None], [542, 31]])
test_function([[1, 4, 3, None], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
