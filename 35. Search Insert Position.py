
# 二分法，套模版
class Solution:  # 找第一个 >= target 的数字的位置。可以插的位置有 n+1 个
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return 0
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] >= target: return left
        if nums[right] >= target: return right
        return right + 1
