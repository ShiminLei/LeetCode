# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这道题主要是一个递归的思想，关键就是怎么构思出来 递归的构造
def pathSumFrom(node, sum):  # 从某个点开始加，有几条路
    if not node: return 0
    return int(node.val == sum) + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val);


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        return pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)




