class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [[]]
        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])  # 这里涉及数组的深度拷贝问题
                    ans[i].append(char.lower())
                    ans[n + i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return list(map("".join, ans))  # 批量处理的时候，可以用map

    # 心得： 其实 list.copy() 和 list[:] 的效果是一样的