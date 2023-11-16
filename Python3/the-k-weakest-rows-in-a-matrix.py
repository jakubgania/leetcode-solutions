# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = {}

        for index in range(len(mat)):
            arr[index] = mat[index].count(1)

        arr_sorted = dict(sorted(arr.items(), key=lambda item: item[1]))

        return list(arr_sorted.keys())[0:k]