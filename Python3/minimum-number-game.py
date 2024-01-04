# https://leetcode.com/problems/minimum-number-game/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []

        nums.sort()

        while len(nums) / 2:
            ans.append(nums[1])
            ans.append(nums[0])
            nums.remove(nums[0])
            nums.remove(nums[0])

        return ans