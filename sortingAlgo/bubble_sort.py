def bubble_sort(array):
    itr = 0

    def helper_func(array,itr):
        if itr == len(array):
            return array
        swapped = False
        for i in range(len(array) - itr - 1):
            print(array,array[i],array[i + 1])
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            return array
        
        return helper_func(array,itr+1)

    return helper_func(array, itr)

print(bubble_sort([8,1,2,3,4,5,6,7]))
