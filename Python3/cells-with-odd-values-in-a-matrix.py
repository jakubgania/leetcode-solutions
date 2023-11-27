# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        x, y = [0] * m,[0] * n
    
        for r, c in indices:
            x[r] += 1
            y[c] += 1
        
        return sum([ (r + c) % 2 for c in y for r in x])  