# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from bisect import bisect
class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        # 可以先用二分搜索查找插入位置，再合并
        index = bisect([i.start for i in intervals], newInterval.start)
        intervals.insert(index, newInterval)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged

