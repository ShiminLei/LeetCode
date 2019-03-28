
from bisect import bisect
class Solution:
    # 对于每一个房子，找到供暖设备中离它最近的
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0

        for h in houses:
            hi = bisect(heaters, h)# index 返回的是，h需要插入的位置, heaters本身并不会被改变
            left = heaters[hi-1] if hi - 1 >= 0 else float('-inf') # house 左边hearter的位置
            right = heaters[hi] if hi < len(heaters) else float('inf') # house 右边hearter的位置
            ans = max(ans, min(h - left, right - h))

        return ans