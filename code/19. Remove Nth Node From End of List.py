# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        p1 = head
        p2 = head
        for _ in range(n):
            p2 = p2.next
        if not p2:
            return head.next
        while p2 is not None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
