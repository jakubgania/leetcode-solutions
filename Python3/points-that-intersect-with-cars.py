# https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums_set = set()

        for item in nums:
            for item_range in range(item[0], item[1] + 1):
                nums_set.add(item_range)

        return len(nums_set)