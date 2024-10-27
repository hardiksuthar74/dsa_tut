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

    
             

if __name__ == "__main__":
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
        print(binary_search([1,2,3,4,5,6,7],x))
    else:
        print("Please provide x")
