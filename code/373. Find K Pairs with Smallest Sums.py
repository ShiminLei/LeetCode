class Solution:
    # 这道题每个list k+1 的数字是不用考虑的
    def kSmallestPairs(self, nums1, nums2, k):
        queue = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs


class Solution:
    # 这道题每个list k+1 的数字是不用考虑的
    def kSmallestPairs(self, nums1, nums2, k):
        return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2), key=sum)
