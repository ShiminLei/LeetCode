

class Solution:
    # 这一题用的是回溯法，其本质思想是dfs
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(nums, target, path, index, ans):
            if target < 0: return
            if target == 0: ans.append(path)
            for i in range(index, len(nums)):
                dfs(nums, target - nums[i], path + [nums[i]], i, ans)

        ans = []
        dfs(candidates, target, [], 0, ans)
        return ans