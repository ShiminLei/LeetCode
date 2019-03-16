# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sametree(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return node1.val==node2.val and sametree(node1.left, node2.left) and sametree(node1.right, node2.right)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if sametree(s,t):
            return True
        if not s:
            return False
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)