# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeaf(self, node):
        if node.right is None and node.left is None:
            return True
        else:
            return False

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if self.isLeaf(root):
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        elif root.right and not root.left:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min([self.minDepth(root.left), self.minDepth(root.right)])