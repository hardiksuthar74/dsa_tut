def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid_point = len(nums) // 2
    nums1 = merge_sort(nums[:mid_point])
    nums2 = merge_sort(nums[mid_point:])
    return merging(nums1,nums2)

def merging(nums1,nums2):
    sorted_array = []

    pointer_one = 0
    pointer_two = 0

    while pointer_one < len(nums1) and pointer_two < len(nums2):
        if nums1[pointer_one] < nums2[pointer_two]:
            sorted_array.append(nums1[pointer_one])
            pointer_one += 1
        else:
            sorted_array.append(nums2[pointer_two])
            pointer_two += 1
    
    while pointer_one < len(nums1):
        sorted_array.append(nums1[pointer_one])
        pointer_one += 1

    while pointer_two < len(nums2):
        sorted_array.append(nums2[pointer_two])
        pointer_two += 1

    return sorted_array

print(merge_sort([2,3,1,5,6,1,3,8,10,1,12,2,21]))

