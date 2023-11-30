# https://leetcode.com/problems/array-partition/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()

        for index in range(0, len(nums), 2):
            ans += min(nums[index], nums[index + 1])

        return ans