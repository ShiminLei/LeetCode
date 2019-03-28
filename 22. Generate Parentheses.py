# https://www.bilibili.com/video/av45844036?from=search&seid=15209021753482192329
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n: backtrack(S+'(', left+1, right)
            if right < left: backtrack(S+')', left, right+1)

        backtrack()
        return ans