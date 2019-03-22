from heapq import *


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))

        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return min(nums)

        heap = nums[:3]
        heapify(heap)
        for i in nums[3:]:
            heappushpop(heap, i)

        return min(heap)
