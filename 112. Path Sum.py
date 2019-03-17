# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)