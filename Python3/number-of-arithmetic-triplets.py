# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans, nums_len = 0, len(nums)

        for i in range(nums_len):
            for j in range(i, nums_len):
                for k in range(j, nums_len):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff and i < j < k:
                        ans += 1

        return ans