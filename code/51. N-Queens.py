class Solution:  # 皇后的攻击范围是，一行，一列，对角线
    def solveNQueens(self, n: int) -> List[List[str]]:  # 这个题用到回溯

        # nums is a one-dimension array, like [1, 3, 0, 2] means first queen is placed in column 1, second queen is placed in column 3, etc. 把 nums 竖着看
        def dfs(nums, index, path, res):  # path = [] 试探index行的放置
            if index == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                nums[index] = i  # 第index 行的皇后，放在第i 列
                if valid(nums, index):  # 检验刚才放的第 index行的放置，是否合理
                    tmp = "." * len(nums)
                    dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)

        def valid(nums, index): #检查第 n 行的放置是否合理
            for i in range(index): # 只和n行之前的行进行对比，看是否valid
                if abs(nums[i] - nums[index]) == index - i or nums[i] == nums[index]:
                    return False  # 如果两个位置列数之差的绝对值等于行数差(在同一条对角线)，或列数相等，那么他们相互攻击
            return True

        res = []
        dfs([-1] * n, 0, [], res)
        return res



