class Solution:
    def reverse(self, x: int) -> int:
        sign = (x>0)-(x<0)
        res = int(str(sign*x)[::-1])
        return (res < 1<<31)*res*sign
