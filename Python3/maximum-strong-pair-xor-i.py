# https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        nums_len = len(nums)

        for index1 in range(nums_len):
            for index2 in range(index1, nums_len):
                if abs(nums[index1] - nums[index2]) <= min(nums[index1], nums[index2]):
                    xor_val = nums[index1] ^ nums[index2]
                    if xor_val > ans:
                        ans = xor_val

        return ans