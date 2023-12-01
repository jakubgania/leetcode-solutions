# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def blank(x, y):
            if (x < 0) or (x >= len(grid)) or (y < 0) or (y >= len(grid[0])) or grid[x][y] == 0:
                return 0

            grid[x][y] = 0

            return 1 + blank(x - 1, y) + blank(x + 1, y) + blank(x, y - 1) + blank(x, y + 1)

        ans = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    temp = blank(i, j)
                    if temp > ans:
                        ans = temp

        return ans