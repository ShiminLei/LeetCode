
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def set_intersection(set1, set2):
            return [x for x in set1 if x in set2]

        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return set_intersection(set1, set2)
        else:
            return set_intersection(set2, set1)