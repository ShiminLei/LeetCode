
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower = -1 << 31 # lower = -float('inf') 也可以，总之就是无限小的意思
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True



# def verifyPreorder( preorder):
#     stack = []
#     lower = -1 << 31
#     for x in preorder:
#         if x < lower:
#             return False
#         while stack and x > stack[-1]:
#             print(stack)
#             lower = stack.pop()
#             print(lower)
#         stack.append(x)
#         print(stack)
#         print('----')
#     return True
# verifyPreorder([5,2,1,3,6])

# [5]
# ----
# [5, 2]
# ----
# [5, 2, 1]
# ----
# [5, 2, 1]
# 1
# [5, 2]
# 2
# [5, 3]
# ----
# [5, 3]
# 3
# [5]
# 5
# [6]
#----