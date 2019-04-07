class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)  # 活用sort 和 lambda!!

        return points[:K]

# from collections import defaultdict
# import heapq
# class Solution(object):
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
#         lst = []
#         dic = defaultdict(list)
#         for i,j in points:
#             a = i**2+j**2
#             lst.append(a)
#             dic[a].append((i,j))
#         heap = [float('-inf')]*K
#         for i in lst:
#             num = heapq.heappop(heap)
#             heapq.heappush(heap,max(-i,num))
#             heapq.heapify(heap)
#         res = []
#         for item in heap:
#             res.append(dic[-item].pop())
#         return res