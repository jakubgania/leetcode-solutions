# https://leetcode.com/problems/strictly-palindromic-number/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for item in range(2, n - 2 + 1):
            temp, digits = n, []
    
            while temp:
                digits.append(int(temp % item))
                temp //= item

            number = ''.join(map(str, digits[::1]))

            if str(number) != reversed(str(number)):
                return False

        return True