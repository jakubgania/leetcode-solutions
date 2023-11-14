# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans, grid_len = [], len(grid)
        
        for index_1 in range(0, grid_len - 3 + 1):
            temp_arr = []
            for index_2 in range(0, grid_len - 3 + 1):
                temp = grid[index_1][index_2]
                for index_3 in range(index_1, index_1 + 3):
                    for index_4 in range(index_2, index_2 + 3):
                        if grid[index_3][index_4] > temp:
                            temp = grid[index_3][index_4]
                temp_arr.append(temp)
            ans.append(temp_arr)

        return ans