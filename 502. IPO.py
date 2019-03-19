class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        current = []
        future = sorted(zip(Capital, Profits))[::-1] # 按照capital从大到小排列
        for _ in range(k):
            while future and future[-1][0] <= W: # 当capital最小的，比W小的时候，可以放candidate。这是一个装candidate的过程
                heapq.heappush(current, -future.pop()[1]) # current 是一个max heap，装profit
            if current:  # 这里可能面临 current为空  # 这里pop出来的是future最后的元素，就是capital最小的pair
                W -= heapq.heappop(current)
        return W