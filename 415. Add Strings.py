class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total1 = ord(num1[0]) - 48
        for i in num1[1:]:
            num = ord(i) - 48
            total1 = total1 * 10 + num
        total2 = ord(num2[0]) - 48
        for i in num2[1:]:
            num = ord(i) - 48
            total2 = total2 * 10 + num
        total = total1 + total2
        if total == 0:
            return "0"
        text = ""
        while total != 0:
            total, remain = divmod(total, 10)
            text += (chr(remain + 48))
        return text[::-1]



