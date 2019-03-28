class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        lbound, rbound = -1, -1

        # for the left one
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            lbound = left
        elif nums[right] == target:
            lbound = right
        else:
            return [-1, -1]

        # for the right one
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid  # 这里不一样
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] == target:  # 这里不一样，先right,
            rbound = right
        elif nums[left] == target:
            rbound = left
        else:
            return [-1, -1]

        return [lbound, rbound]

