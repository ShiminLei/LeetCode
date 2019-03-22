class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for i in str:
            if ord(i) >= 65 and ord(i) <= 90:
                res += (chr(ord(i) + 32))
            else:
                res += i
            print(res)
        return res
