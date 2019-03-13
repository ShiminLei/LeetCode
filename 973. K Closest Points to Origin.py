class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)  # 活用sort 和 lambda!!

        return points[:K]