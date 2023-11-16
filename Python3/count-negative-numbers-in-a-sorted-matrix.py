# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans, grid_height, grid_width, column = 0, len(grid), len(grid[0]), 0

        for index in range(grid_height - 1, -1, -1):
            while column < grid_width and grid[index][column] >= 0:
                column += 1
            ans += grid_width - column
        
        return ans