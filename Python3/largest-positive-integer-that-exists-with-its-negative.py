# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        temp = []
        nums.sort()
        nums_set = set(nums)

        for item in nums:
            if item >= 0:
                break

            item_abs = abs(item)
            if item_abs in nums_set:
                temp.append(item_abs)

        if temp:
            return temp[0]

        return -1