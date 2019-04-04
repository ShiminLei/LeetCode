
class Solution: # 分治法
    def findPeakElement(self, nums: List[int]) -> int:
        def search(nums, left, right):
            if left == right: return left
            mid = left+(right-left)//2
            if nums[mid] < nums[mid+1]:
                return search(nums, mid+1, right)
            else:
                return search(nums,left, mid)
        return search(nums,0, len(nums)-1)