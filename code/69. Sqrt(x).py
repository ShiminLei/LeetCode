
class Solution:
    def mySqrt(self, x: int) -> int:
        if x== 0:
            return 0
        left, right = 0, x
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                left = mid
            else:
                right = mid
        if right ** 2 > x:
            return left
        else:
            return right
