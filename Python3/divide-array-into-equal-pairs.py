# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        for item in nums_set:
            if nums.count(item) % 2 != 0:
                return False

        return True