class Solution:
    # 回溯法的本质是搜索树
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first=0):
            if first == n:
                new = nums[:]
                if new not in output:
                    output.append(new)
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output