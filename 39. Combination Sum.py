class Solution:  # 回溯法
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(nums, target, path, index, ans):
            if target < 0: return
            if target == 0: ans.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(nums, target - nums[i], path, i, ans)
                path.pop()

        ans = []
        dfs(candidates, target, [], 0, ans)
        return ans