# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            return TreeNode(root.val)
        t = TreeNode(root.val)
        t.right = self.invertTree(root.left)
        t.left = self.invertTree(root.right)
        return t