class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        wide = len(matrix)
        for i in range(wide): # 先沿着左上到右下的对角线反转，
            for j in range(i,wide):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:  # 再左右翻转
            row.reverse()