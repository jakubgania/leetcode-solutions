# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0

        for index in range(n):
            ans ^= start + (2 * index)

        return ans