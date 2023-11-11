# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return sum([max(nums) + i for i in range(k)])