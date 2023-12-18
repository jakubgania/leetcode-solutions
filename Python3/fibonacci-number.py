# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        number_0, number_1 = 0, 1

        for item in range(2, n + 1):
            temp = number_0 + number_1
            number_0, number_1 = number_1, temp
        
        return temp