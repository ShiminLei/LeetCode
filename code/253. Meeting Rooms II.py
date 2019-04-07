# https://www.youtube.com/watch?v=GmpyAMpjpUY  这个视频讲的可以

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        free_rooms = []  # 这个堆存的是，每个房间最后活动的结束时间
        # intervals按照开始时间从小到大排序
        intervals.sort(key=lambda x: x.start)
        # 把第一个开始时间的活动结束时间 push到 堆里
        heapq.heappush(free_rooms, intervals[0].end)
        for i in intervals[1:]:
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)  # pop掉堆的最小值
            heapq.heappush(free_rooms, i.end)
        return len(free_rooms)


