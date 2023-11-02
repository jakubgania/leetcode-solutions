# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''.join([str(x) for x in digits])
        x = int(x) + 1
        x = [int(n) for n in str(x)]
        
        return x