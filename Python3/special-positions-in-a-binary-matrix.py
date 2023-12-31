# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        
        def checkColumn(column):
            temp = 0

            for index in range(len(mat)):
                if temp > 1:
                    return 2
                elif mat[index][column] == 1:
                    temp += 1

            return temp

        for row in range(len(mat)):
            for cell_index in range(len(mat[row])):
                if mat[row][cell_index] == 1:
                    if mat[row].count(1) == 1 and checkColumn(cell_index) == 1:
                        ans += 1

        return ans