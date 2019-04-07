
class Solution(object):  # 这是一道非常典型的二分法的题目，可以套用万门模版
    def findMin(self, nums): # 找最小 min
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return -1
        left, right = 0, len(nums) - 1
        while left+1 < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = left + (right-left)//2
            if nums[mid]>=nums[left]:
                left = mid+1
            else:
                right = mid
        return min(nums)