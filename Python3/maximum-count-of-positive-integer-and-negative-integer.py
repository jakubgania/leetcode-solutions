# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ans, zero = 0, 0

        for item in nums:
            if item < 0:
                ans += 1

            if item == 0:
                zero += 1

            if item > 0:
                break

        if len(nums) - ans - zero > ans:
            return len(nums) - ans - zero

        return ans