# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        cols = Counter([tuple(col) for col in grid])

        for row in zip(*grid):
            ans += cols[row]

        return ans