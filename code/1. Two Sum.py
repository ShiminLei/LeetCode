class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, n in enumerate(nums):
            if (target - n) in seen:
                return [i, seen[target - n]]
            else:
                seen[n] = i

