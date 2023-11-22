# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans, nums_len = 0, len(nums)
    
        for i in range(nums_len):
            for j in range(i + 1, nums_len + 1):
                ans += len(set(nums[i:j])) ** 2

        return ans