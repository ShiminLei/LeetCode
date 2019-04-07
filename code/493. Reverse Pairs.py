def merge_sort(A, l, r):
    if l < r:
        m = l + (r - l) // 2
        count = merge_sort(A, l, m) + merge_sort(A, m + 1, r)
        i, j = l, m + 1
        for i in range(l, m + 1):
            while A[i] > A[j] * 2 and j < r:
                j += 1
            if j == r and A[i] > A[j] * 2:
                count += j - m  # 这里的条件注意一下！！2倍大哦！！！
            else:
                count += j - m - 1
        merge(A, l, m, r)
        return count
    else:
        return 0


def merge(A, l, m, r):
    list1 = A[l:m + 1] + [float('inf')]
    list2 = A[m + 1:r + 1] + [float('inf')]
    i, j = 0, 0
    for k in range(l, r + 1):
        if list1[i] <= list2[j]:
            A[k] = list1[i]
            i += 1
        else:
            A[k] = list2[j]
            j += 1


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return merge_sort(nums, 0, len(nums) - 1)