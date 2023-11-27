# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = num
        
        if num < 10:
            return True

        reversal = int(str(num).strip("0").rstrip("0")[::-1][::-1])
        
        return reversal == temp