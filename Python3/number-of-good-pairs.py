# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans, nums_len = 0, len(nums)

        for index1 in range(0, nums_len):
            for index2 in range(1, nums_len):
                if nums[index1] == nums[index2] and index1 < index2:
                    ans += 1

        return ans