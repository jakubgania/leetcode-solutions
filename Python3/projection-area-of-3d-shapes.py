# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0

        for a in zip(*grid):
            ans += max(a)

        for item in grid:
            ans += max(item)

        ans += sum([1 for item in grid for x in item if x > 0])

        return ans