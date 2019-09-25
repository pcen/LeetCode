def driver():
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))

class Solution:
    def twoSum(self, nums, target):
        paired_indexes = {}
        for i, num in enumerate(nums):
            if num in paired_indexes:
                return [paired_indexes[num], i]
            else:
                paired_indexes[target - num] = i

driver()
