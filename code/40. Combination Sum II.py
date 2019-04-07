class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(nums, target, path, index, ans):
            if target < 0: return
            if target == 0: ans.append(path[:])
            for i in range(index, len(nums)):
                if ( i >index and nums[i ]== nums[ i -1]):  # 这里需要有判断条件，如果前面算过了，后面不用再算
                    continue
                path.append(nums[i])
                dfs(nums, target -nums[i], path , i +1 ,ans) # 这里是i+1
                path.pop()

        ans = []
        candidates.sort()  # 这里需要 sort
        dfs(candidates, target, [], 0, ans)
        return ans

