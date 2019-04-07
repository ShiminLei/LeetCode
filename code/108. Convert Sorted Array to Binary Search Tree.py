# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        middle = len(nums) // 2
        t = TreeNode(nums[middle])

        t.left = self.sortedArrayToBST(nums[:middle])
        t.right = self.sortedArrayToBST(nums[middle + 1:])

        return t