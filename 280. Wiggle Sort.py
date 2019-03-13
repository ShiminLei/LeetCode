class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        这一题不让 return 任何数值，直接在原值上改。
        """
        nums.sort()
        i = 1
        while i < len(nums)-1:
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i += 2
