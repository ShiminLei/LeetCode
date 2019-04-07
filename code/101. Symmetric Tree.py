
# 简洁的方法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def ismirror(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return node1.val == node2.val and ismirror(node1.left, node2.right) and ismirror(node1.right, node2.left)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return ismirror(root, root)


# 第一次自己写的
# def mirror(node):
#     if not node:
#         return
#     node.left, node.right = node.right, node.left
#     mirror(node.left)
#     mirror(node.right)
#
#
# def sametree(node1, node2):
#     if not node1 and not node2:
#         return True
#     if not node1 or not node2:
#         return False
#     return node1.val == node2.val and sametree(node1.left, node2.left) and sametree(node1.right, node2.right)
#
#
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         mirror(root.left)
#         return sametree(root.left, root.right)
