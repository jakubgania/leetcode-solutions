# https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff = []

        for i in range(len(nums)):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            diff.append(prefix-suffix)

        return diff