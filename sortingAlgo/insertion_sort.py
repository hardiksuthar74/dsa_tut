def insertion_sort(nums):
    for i in range(1, len(nums)):
        current_val = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > current_val:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = current_val

    return nums

print(insertion_sort([13,122,38,49,41,57,16]))
