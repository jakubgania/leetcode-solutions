# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans, t, j = [0] * nums_len, 0, nums[0]
        nums.append(None)

        for index in range(nums_len):            
            t += nums[index] + j
            ans[index] = t

            if nums[index + 1] != None and j < nums[index + 1]:
                j = nums[index + 1]

        return ans