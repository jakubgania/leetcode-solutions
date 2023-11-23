# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        temp_sum_1, temp_sum_2 = 0, 0

        for i in range(1, n + 1):
            temp_sum_1 = sum(range(1, i + 1))
            temp_sum_2 = sum(range(i, n + 1))

            if temp_sum_1 == temp_sum_2:
                return i

        return -1