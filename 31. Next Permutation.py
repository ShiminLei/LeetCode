class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start):
            i = start
            j = len(nums) - 1
            while (i < j):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:  # 就是说不是最后一个排列，不是完全倒序了
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        reverse(nums, i + 1)

