# class Solution: # 递归法
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         if not nums: return [[]]
#         res_subsets = self.subsets(nums[1:])
#         return res_subsets + [[nums[0]]+i for i in res_subsets]

class Solution:  # 回溯法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets_recursive_helper(result, lst, nums, pos):
            result.append(lst[:])
            for i in range(pos, len(nums)):
                lst.append(nums[i])  #
                subsets_recursive_helper(result, lst, nums, i + 1)  #
                lst.pop()

        lst = []
        result = []
        subsets_recursive_helper(result, lst, nums, 0);
        return result

