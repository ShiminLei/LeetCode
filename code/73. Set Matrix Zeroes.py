class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        record = []
        C = len(matrix)
        R = len(matrix[0])
        for i in range(C):
            for j in range(R):
                if matrix[i][j] == 0:
                    record.append([i, j])
        for rec in record:
            for c in range(C):
                matrix[c][rec[1]] = 0
            for r in range(R):
                matrix[rec[0]][r] = 0

