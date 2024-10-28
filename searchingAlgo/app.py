import sys

#example of linear search in python

def linear_search(array,el):
    array_len = len(array)

    for i in range(array_len):
        if array[i] == el:
            return i

    return -1

def binary_search(array,x):
    left_pointer = 0
    right_pointer = len(array) - 1
    middle_el = (left_pointer + right_pointer) // 2

    while left_pointer <= right_pointer:
        if array[middle_el] > x:
            right_pointer = middle_el - 1
        else:
            left_pointer = middle_el + 1
        middle_el = (left_pointer + right_pointer) // 2

    return middle_el if array[middle_el] == x else -1

def naive_string_search(string,value):
    check_pointer = 0
    total_count = 0
    for i in string:
        if i == value[check_pointer]:
            check_pointer += 1
        else:
            check_pointer = 0
        
        if len(value) == check_pointer:
            total_count += 1
            check_pointer = 0

    
    print(string)
    print(value)
    return total_count
             

if __name__ == "__main__":
    print(naive_string_search("lorie loled","lo"))
