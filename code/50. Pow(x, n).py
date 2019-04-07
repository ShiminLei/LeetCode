
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_power(x: float, n: int):
            if n == 0: return 1
            half = fast_power(x, n // 2);
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n >= 0:
            return fast_power(x, n)
        else:
            return 1 / fast_power(x, -n)



