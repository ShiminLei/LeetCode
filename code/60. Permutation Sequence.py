import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1             # 之所以-1是因为，如果不-1的话，正好 k 除尽阶乘的时候，其实还没有进位到下一个数, 而index却进了一位
        while n > 0:
            n -= 1 # n是后面的 sub array有几位
            # get the index of current digit
            index, k = divmod(k, math.factorial(n)) # 计算阶乘 math.factorial
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation