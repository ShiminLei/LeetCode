class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        res_subsets = self.subsets(nums[1:])
        return res_subsets + [[nums[0]] + i for i in res_subsets]

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sets = self.subsets(nums)
        sets = [sorted(i) for i in sets]
        ans = []
        for i in sets:
            if i not in ans:
                ans.append(i)
        return ans
