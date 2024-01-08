# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        value = x ^ y
        distance = 0

        while value > 0:
            value = value & (value - 1)
            distance += 1

        return distance