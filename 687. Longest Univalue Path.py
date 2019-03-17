# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def find(node, val):
    if not node or node.val != val:
        return 0
    else:
        return 1 + max(find(node.left, val), find(node.right, val))


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        # 情况1:root属于longest path
        max_from_root = find(root.left, root.val) + find(root.right, root.val)
        #  情况2: root 不属于 longest path
        max_not_root = max(self.longestUnivaluePath(root.right), self.longestUnivaluePath(root.left))
        return max(max_from_root, max_not_root)

