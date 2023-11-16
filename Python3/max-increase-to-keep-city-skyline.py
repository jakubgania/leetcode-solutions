# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        arr_max_row_values = []
        arr_max_col_values = []

        for item in grid:
            arr_max_col_values.append(max(item))

        for item in zip(*grid):
            arr_max_row_values.append(max(item))

        for i in range(len(grid)):
            for j in range(len(grid)):
                ans += abs(grid[i][j] - min(arr_max_row_values[j], arr_max_col_values[i]))

        return ans