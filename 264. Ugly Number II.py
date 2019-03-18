


class Solution:
    def nthUglyNumber(self, n):
        min_heap = [1]
        last = 0 # last 指的是当前数之前，最大被pop出去的数
        cnt = 0
        while cnt < n:
            i = heapq.heappop(min_heap)
            if i <= last: continue #skip duplicates
            last = i
            cnt += 1
            if cnt == n: return i
            heapq.heappush(min_heap, i*2)
            heapq.heappush(min_heap, i*3)
            heapq.heappush(min_heap, i*5)


# # 一个非常简洁的写法
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         q2, q3, q5 = [2], [3], [5]
#         ugly = 1
#         for u in heapq.merge(q2, q3, q5):
#             if n == 1:
#                 return ugly
#             if u > ugly:
#                 ugly = u
#                 n -= 1
#                 q2 += 2 * u,
#                 q3 += 3 * u,
#                 q5 += 5 * u,