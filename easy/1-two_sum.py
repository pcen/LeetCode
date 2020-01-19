def twoSum(nums, target):
    paired_indexes = {}
    for i, num in enumerate(nums):
        if num in paired_indexes:
            return [paired_indexes[num], i]
        else:
            paired_indexes[target - num] = i

