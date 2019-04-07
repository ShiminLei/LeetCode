# 答案的方法，很简单
def findSecondMinimumValue(self, root):
    self.ans = float('inf')
    min1 = root.val

    def dfs(node):
        if node:
            if min1 < node.val < self.ans:
                self.ans = node.val
            elif node.val == min1:
                dfs(node.left)
                dfs(node.right)

    dfs(root)
    return self.ans if self.ans < float('inf') else -1


# 自己写的方法，比较复杂
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def findSecondMinimumValue(self, root: TreeNode) -> int:
#         if not root:
#             return -1
#         if not root.left and not root.right:
#             return -1
#
#         left = self.findSecondMinimumValue(root.left)
#         right = self.findSecondMinimumValue(root.right)
#         # 以下就是一个有两个子节点了
#         if root.left.val < root.right.val:
#             if left == -1:
#                 return root.right.val
#             else:
#                 return min(left, root.right.val)
#         elif root.left.val > root.right.val:
#             if right == -1:
#                 return root.left.val
#             else:
#                 return min(right, root.left.val)
#         else:
#             if left == -1 and right == -1:
#                 return -1
#             elif left == -1 and right != -1:
#                 return right
#             elif left != -1 and right == -1:
#                 return left
#             else:
#                 return min(left, right)