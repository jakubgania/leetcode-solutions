# https://leetcode.com/problems/number-of-common-factors/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter = 0
        min_num = min(a , b)

        for item in range(1, min_num + 1):
            if a % item == 0 and b % item == 0:
                counter += 1

        return counter