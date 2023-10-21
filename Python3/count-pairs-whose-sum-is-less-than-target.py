# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i, ans, nums_length = 0, 0, len(nums)

        while(i < nums_length - 1):
            for j in range(i + 1, nums_length):
                if nums[i] + nums[j] < target:
                    ans += 1
            i += 1

        return ans