# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ValueinTree(self, value, root):
        if root is None:
            return True
        if value != root.val:
            return False
        else:
            return self.ValueinTree(value, root.left) and self.ValueinTree(value, root.right)

    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        if self.ValueinTree(value, root.left) and self.ValueinTree(value, root.right):
            return True
        else:
            return False

