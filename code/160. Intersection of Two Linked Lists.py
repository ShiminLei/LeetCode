# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB: return None

        a = headA
        b = headB

        while a is not b:  # 如果是不相交的话，最后会一起到 None
            a = a.next if a is not None else headB
            b = b.next if b is not None else headA

        return a

