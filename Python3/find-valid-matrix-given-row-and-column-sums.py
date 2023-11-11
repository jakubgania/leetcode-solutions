# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row_len, col_len = len(rowSum), len(colSum)
        ans = [[0 for i in range(col_len)] for j in range(row_len)]

        for row_index in range(row_len):
            for col_index in range(col_len):
                temp = min(rowSum[row_index], colSum[col_index])
                ans[row_index][col_index] = temp
                rowSum[row_index] -= temp
                colSum[col_index] -= temp

        return ans