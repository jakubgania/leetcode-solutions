# https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans, counter = 0, 0

        while len(grid[0]) >= 1:
            temp_arr = []
            for index in range(len(grid)):
                temp_max = max(grid[index])
                temp_arr.append(temp_max)
                grid[index].pop(grid[index].index(temp_max))

            ans += max(temp_arr)

        return ans