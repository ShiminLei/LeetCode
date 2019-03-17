"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def pos(node):
            if not node:
                return
            for child in node.children:
                pos(child)
            ans.append(node.val)

        pos(root)
        return ans
