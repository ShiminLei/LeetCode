
# https://ask.julyedu.com/question/7299
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the intersection point of two pointer
        slow = nums[0] # 相当于一个存着下个位置坐标的指针
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # find the entrance to the cycle
        p1 = nums[0]
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1