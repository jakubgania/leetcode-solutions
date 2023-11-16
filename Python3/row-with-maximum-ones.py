# https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = []

        index = 0
        count = mat[0].count(1)

        for loop_index in range(1, len(mat)):
            temp_count = mat[loop_index].count(1)
            if temp_count > count:
                index, count = loop_index, temp_count

        return [index, count]
