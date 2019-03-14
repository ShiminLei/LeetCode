# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, root, k, dic):  # dic 传入的是指针，所以可以直接改变
        if not root:
            return False
        if k - root.val in dic:
            return True
        dic[root.val] = 1
        return self.find(root.left, k, dic) or self.find(root.right, k, dic)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        dic = {}
        return self.find(root, k, dic)
