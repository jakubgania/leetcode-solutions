# https://leetcode.com/problems/sqrtx/

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: 
            return x

        temp = len(str(x)) * pow(10, 2)

        # for a larger number of cycles the accuracy is better
        for index in range(10):
            temp = (1/2) * (temp + (x / temp))

        return math.floor(temp)
        