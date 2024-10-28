def bubble_sort(array):
    itr = 0

    def helper_func(array,itr):
        if itr == len(array):
            return array

        for i in range(len(array) - itr - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        return helper_func(array,itr+1)

    return helper_func(array, itr)

print(bubble_sort([241,111,223,45,151,1,19,2,3,45,78]))
