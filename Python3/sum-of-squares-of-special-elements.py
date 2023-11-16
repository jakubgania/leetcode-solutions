# https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        nums_len = len(nums)

        for index in range(1, nums_len + 1):
            if nums_len % index == 0:
                ans += nums[index - 1] ** 2

        return ans