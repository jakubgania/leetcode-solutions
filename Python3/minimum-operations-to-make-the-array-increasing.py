# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for i in range(1, len(nums)):
            temp = nums[i]
            nums[i] = max(nums[i - 1] + 1, nums[i])
            ans += nums[i] - temp

        return ans