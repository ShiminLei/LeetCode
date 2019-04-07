class Solution:  # 可以用空间缩减的方式
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        height = len(matrix)
        width = len(matrix[0])

        # 在这个matrix里面，大多数找比它大或小的数，都有两个方向选择
        # 只有左下角的数，有一个方向选择，这样可以走一步 划一行 或者 划一列
        row = height - 1
        col = 0

        while col < width and row >= 0:  # 从左下角，往右斜上走
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False



