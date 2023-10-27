# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        num_a, num_b, digits = 0, 0, []
        
        for digit in str(num):
            digits.append(int(digit))

        digits = sorted(digits)

        if digits[2] > 0:
            num_a = int(str(digits[0]) + str(digits[2]))
        else:
            num_a = digits[0]

        if digits[3] > 0:
            num_b = int(str(digits[1]) + str(digits[3]))
        else:
            num_b = digits[1]
        
        return num_a + num_b