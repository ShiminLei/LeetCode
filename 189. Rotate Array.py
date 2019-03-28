class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        if k is None or k <= 0: return
        k, end = k % len(nums), len(nums) - 1
        reverse(nums, 0, end)
        reverse(nums, 0, k - 1)
        reverse(nums, k, end)

