# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for counter in range(len(nums)):
            target.insert(index[counter], nums[counter])

        return target
        