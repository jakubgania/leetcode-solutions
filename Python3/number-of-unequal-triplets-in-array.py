# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        nums_len = len(nums)

        for i in range(0, nums_len - 2):
            for j in range(i, nums_len - 1):
                if nums[i] != nums[j]:
                    for k in range(j, nums_len):
                        if nums[i] != nums[k] and nums[j] != nums[k]:
                            ans += 1

        return ans