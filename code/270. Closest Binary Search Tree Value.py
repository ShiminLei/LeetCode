
# 答案的方法
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closestValue(kid,target)
        return min((a,b), key= lambda x: abs(x-target))


# 自己写的
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if (not root.right and not root.left) or root.val == target:
            return root.val

        elif (root.right and root.val < target) or ((not root.left) and root.right):
            closest_right = self.closestValue(root.right, target)
            if abs(root.val - target) <= abs(closest_right - target):
                return root.val
            else:
                return closest_right
        else:
            closest_left = self.closestValue(root.left, target)
            if abs(root.val - target) <= abs(closest_left - target):
                return root.val
            else:
                return closest_left

