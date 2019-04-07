class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        dic = {}
        dic[0] = 1
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in dic:  # dic 包含了所有之前从0 continue的sum,
                count += dic[summ - k]  # sum-dic是挪一步之后，i+1个新生成的连着的和
            if summ in dic:
                dic[summ] += 1
            else:
                dic[summ] = 1
        return count

