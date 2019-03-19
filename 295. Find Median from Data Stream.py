
 # 这一题的难点在于是数据流，数字的顺序会一直在变，长度也在变

from heapq import * # 这个 import 很省事啊


class MedianFinder:

    def __init__(self):
         self.heaps = [], []

    def addNum(self, num):
         small, large = self.heaps
         heappush(small, -heappushpop(large, num))  # small是个max heap，总是接收负值
         if len(large) < len(small): # 若之前两个 heap的长度就一样，那么在上面的heappush small 之后，large就比small要短了。这种情况是加上num之后，变奇数个总数。
             heappush(large, -heappop(small))

    def findMedian(self):
         small, large = self.heaps
         if len(large) > len(small):  # large 的长度总是大于等于 small
             return float(large[0])
         return (large[0] + (- small[0])) / 2.0




 # Your MedianFinder object will be instantiated and called as such:
 # obj = MedianFinder()
 # obj.addNum(num)
 # param_2 = obj.findMedian()