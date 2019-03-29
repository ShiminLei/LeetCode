class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)  # i是行数，j是列数
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return ret

# from bisect import bisect
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         lo, hi = matrix[0][0], matrix[-1][-1]
#         while lo < hi:
#             mid = lo + (hi - lo) // 2
#             if sum(bisect(row, mid) for row in matrix) < k: # 如果比mid小的数字的和小于k
#                 lo = mid+1
#             else:
#                 hi = mid
#         return lo # 此时其实 lo==hi==mid , 此时比mid小的数字之和正好等于k