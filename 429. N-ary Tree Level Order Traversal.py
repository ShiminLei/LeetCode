"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import defaultdict


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        dic = defaultdict(list)

        def adddict(node, level=0):
            if not node:
                return
            dic[level].append(node.val)
            for child in node.children:
                adddict(child, level + 1)

        adddict(root)
        ans = []
        for key in sorted(dic):
            ans.append(dic[key])
        return ans