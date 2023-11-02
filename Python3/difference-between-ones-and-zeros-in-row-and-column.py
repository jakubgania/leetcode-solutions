# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ans, ones_row_arr, ones_col_arr = [], [], []
        grid_width, grid_height = len(grid[0]), len(grid)

        for index_1 in range(grid_width):
            temp_counter = 0
            for index_2 in range(grid_height):
                if grid[index_2][index_1] == 1:
                    temp_counter += 1
            ones_col_arr.append(temp_counter)

        for index_1 in range(grid_height):
            ones_row_arr.append(grid[index_1].count(1))
            temp_arr = []
            for index_2 in range(grid_width):
                temp_val = ones_row_arr[index_1] + ones_col_arr[index_2] - (grid_height - ones_row_arr[index_1]) - (grid_width - ones_col_arr[index_2])
                temp_arr.append(temp_val)
            ans.append(temp_arr)

        return ans