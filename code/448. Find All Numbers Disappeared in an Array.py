class Solution(object):  # 这个题目很讨巧，就是把出现数字n，作为下标，使nums[n]为负数
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

