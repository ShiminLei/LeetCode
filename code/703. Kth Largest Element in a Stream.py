class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)  # 把一个数字变成一个最小堆
        while len(self.pool) > k:
            heapq.heappop(self.pool)  # 最后剩下k个最大的值

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)  # 先pop，然后再把item加入到堆中，比heappop()再heappush()要快得多

        return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)