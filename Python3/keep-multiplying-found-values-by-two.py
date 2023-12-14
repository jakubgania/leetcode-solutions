# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        if original in nums:
            temp = original
            while temp in nums:
                temp = temp * 2

            return temp
        else:
            return original