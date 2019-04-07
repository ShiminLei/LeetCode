

# 用双指针
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        nums1.sort()
        nums2.sort()
        ans = []
        i,j = 0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                ans.append(nums1[i])
                i+=1  # 两个指针同时移动，可以保证有重复出现
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return ans