class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            carry, remain = divmod(digits[i] + 1 + carry, 10) if i == len(digits) - 1 else divmod(digits[i] + carry, 10)
            digits[i] = remain
            if carry == 0:
                return digits
            else:
                continue
        return [carry] + digits
