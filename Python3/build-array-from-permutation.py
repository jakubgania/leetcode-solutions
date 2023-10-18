#https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[0 for a in range(len(nums))]

        for index in range(len(nums)):
            if 0 <= nums[index] < len(nums):
                ans[index] = nums[nums[index]]

        return ans