# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_counter, neg_counter, ans = 0, 1, [None] * len(nums)

        for item in nums:
            if item > 0:
                ans[pos_counter] = item
                pos_counter += 2
            else:
                ans[neg_counter] = item
                neg_counter += 2
        
        return ans