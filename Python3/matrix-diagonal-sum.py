# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        temp_arr, matrix_len, index_3 = [], len(mat), 0

        for index_1 in range(matrix_len):
            temp_arr.append(mat[index_1][index_1])

        if matrix_len % 2 != 0:
            temp_arr.pop(matrix_len // 2)
        
        for index_2 in range(matrix_len - 1, -1, -1):
            temp_arr.append(mat[index_3][index_2])
            index_3 += 1


        return sum(temp_arr)