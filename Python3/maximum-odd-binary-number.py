# https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zero = s.count('0')
        ans = ''

        if ones > 1:
            for i in range(ones - 1):
                ans += '1'
                

        ans += '0' * zero + '1'

        return ans