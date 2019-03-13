class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A: return []
        odds = []
        evens = []
        for i in A:
            if i%2 == 1:
                odds.append(i)
            else:
                evens.append(i)
        result = []
        for _ in range(len(A)/2):
            result.append(evens[0])
            evens.remove(evens[0])
            result.append(odds[0])
            odds.remove(odds[0])
        return result