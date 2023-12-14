# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            if index % 10 == nums[index]:
                return index

        return -1