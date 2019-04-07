# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        if head is None:
            return 0
        if head.next is None:
            if head.val in G:
                return 1
            else:
                return 0

        summ = 0
        dummy = ListNode(-1)
        dummy.next = head
        status = 'N'
        cur = dummy
        while cur.next is not None:
            prev = status
            cur = cur.next
            if cur.val in G:
                status = 'Y'
            else:
                status = 'N'

            if status == 'Y' and prev == 'N':
                summ += 1
            else:
                pass
        return summ

