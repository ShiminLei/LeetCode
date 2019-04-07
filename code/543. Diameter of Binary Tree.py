# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def longest(node):
    if not node:
        return 0
    if not node.right and not node.left:
        return 1
    return max(longest(node.right), longest(node.left)) + 1


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        return max(longest(root.left) + longest(root.right), self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right))

