# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# # 删除 linklist node 的方法，可以用偷梁换柱法

class Solution:
    def deleteNode(self, node):  # 这里只能访问这个节点
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

