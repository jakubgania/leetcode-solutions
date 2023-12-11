# https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        number = str(bin(n)[2:])[::-1]

        for index in range(len(number)):
            if number[index] == "1":
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1

        return [even, odd]