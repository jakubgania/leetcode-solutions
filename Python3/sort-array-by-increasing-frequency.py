# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums, reverse = 1), key = nums.count)