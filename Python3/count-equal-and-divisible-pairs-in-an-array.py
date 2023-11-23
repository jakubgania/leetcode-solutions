# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans, nums_len = 0, len(nums)

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans += 1

        return ans