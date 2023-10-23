# https://leetcode.com/problems/sum-multiples/

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        temp_arr, div_arr = [], [3,5,7]

        for item in div_arr:
            temp = item
            for index in range(n):
                if temp <= n:
                    temp_arr.append(temp)
                    temp += item

        return sum(list(dict.fromkeys(temp_arr)))