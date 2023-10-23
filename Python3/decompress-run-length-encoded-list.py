# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []

        for index in range(0, len(nums) - 1, 2):
            ans += [nums[index + 1]] * nums[index]

        return ans
        