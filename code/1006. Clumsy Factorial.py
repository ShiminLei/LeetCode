class Solution:
    def clumsy(self, N: int) -> int:
        rest = N % 4
        if rest == 0:
            rest_total = 0
        elif rest == 1:
            rest_total = 1
        elif rest == 2:
            rest_total = 2
        else:
            rest_total = 3 * 2

        if N < 4:
            return rest_total
        else:
            total = int(N * (N - 1) / (N - 2)) + (N - 3)
            for i in range(N - 4, 3, -4):
                total = total - int(i * (i - 1) / (i - 2)) + (i - 3)
            total = total - rest_total
            return total