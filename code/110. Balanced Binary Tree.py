# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:  # 如果是一棵空树，那么是true
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return True
