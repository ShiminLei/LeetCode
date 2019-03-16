# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict  # 这个题，关键是学会怎么用 defaultdict 这个数据结构


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        seen = defaultdict(lambda: defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)
        return ans
