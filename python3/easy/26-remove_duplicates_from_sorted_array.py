def removeDuplicates(nums):
    
    if not nums:
        return 0

    ind = 1
    val = nums[0]
    for i in range(1, len(nums)):
        if not nums[i] == val:
            val = nums[i]
            nums[ind] = val
            ind += 1
    return ind
