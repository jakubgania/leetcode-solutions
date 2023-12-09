# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []

        nums.sort()
        temp = nums.index(target)
        
        return [item for item in range(temp, temp + nums.count(target))]