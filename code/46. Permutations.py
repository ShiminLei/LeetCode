class Solution:
    # 这个题可以用 回溯法， 回溯法的精髓是搜索树
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])  # copy
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output
# 方法2
# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if not nums: return [[]]
#         total = []
#         for i in range(len(nums)):
#             new = nums[:i]+nums[i+1:]
#             total+=[[nums[i]]+sub for sub in self.permute(new)]
#         return total
