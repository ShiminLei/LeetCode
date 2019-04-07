

from bisect import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix == [[]]: return False
        first_column = [row[0] for row in matrix]
        index = bisect(first_column, target)
        if index == 0: return False
        search_row = matrix[index - 1]

        index2 = bisect(search_row, target)
        if index2 - 1 >= 0:
            return target == search_row[index2 - 1]
        else:
            return False