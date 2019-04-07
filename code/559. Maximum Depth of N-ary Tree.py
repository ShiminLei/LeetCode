"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        maximum = 0
        for child in root.children:
            cur = self.maxDepth(child)
            if cur > maximum:
                maximum = cur
        return 1 + maximum

