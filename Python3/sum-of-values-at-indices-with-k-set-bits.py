# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(nums[index] for index in range(len(nums)) if index.bit_count() == k)