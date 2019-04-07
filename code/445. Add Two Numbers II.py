# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []
        while l1 is not None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            list2.append(l2.val)
            l2 = l2.next

        number1 = list1[0]
        for i in list1[1:]:
            number1 = number1 * 10 + i
        number2 = list2[0]
        for i in list2[1:]:
            number2 = number2 * 10 + i

        number = number1 + number2
        if number == 0:
            return ListNode(0)

        list3 = []
        while number != 0:
            number, rest = divmod(number, 10)
            list3.append(rest)
        list3.reverse()

        dummy = ListNode(-1)
        cur = dummy
        for i in list3:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next

