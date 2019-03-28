class Solution:  # 这是一道非常典型的二分搜索的题目
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0: return -1  # 首先需要判断的条件

        left, right = 0, len(nums) - 1  # 设置初始指针
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

