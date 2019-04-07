
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        appear = {n}
        while n!= 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in appear:
                return False
            appear.add(n)
        return True

