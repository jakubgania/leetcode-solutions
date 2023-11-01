# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        ans, num_copy = 0, num

        while num > 0:
            result = num % 10
            if num_copy % result == 0:
                ans += 1
            num = int(num / 10)
        
        return ans