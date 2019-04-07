class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num >= 0 and num < 10:
            return num
        total = 0
        for i in str(num):
            total += int(i)
        return self.addDigits(total)
