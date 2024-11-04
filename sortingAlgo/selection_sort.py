def selection_sort(nums):
    for i in range(len(nums)):
        min_value = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_value]:
                min_value = j
        if min_value != i:
            nums[i], nums[min_value] = nums[min_value], nums[i]
    
    return nums

print(selection_sort([12,3,1,19,8]))
