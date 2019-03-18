class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for k in range(K):
            mini = min(A)
            index = A.index(mini)
            A[index] = -mini
        return sum(A)
