# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head

        dummy = ListNode(-1)
        dummy.next = head
        p = head.next
        maxi = head.val
        end = head  #
        end.next = None  # 把链表截断成两个部分
        while p is not None:
            node = p
            p = p.next
            node.next = None
            if node.val < maxi: # 第一种情况，node需要插到前面的列表
                cur = dummy
                while cur.next.val < node.val:
                    cur = cur.next
                node.next = cur.next
                cur.next = node
            else:                   # 第二种情况，node直接接到前面列表末尾
                end.next = node
                end = end.next
                maxi = node.val

        return dummy.next


# 感想，链表需要定住头和尾




