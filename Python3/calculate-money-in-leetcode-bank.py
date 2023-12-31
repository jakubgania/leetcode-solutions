# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        ans, counter, base = 0, 1, 0

        for item in range(n):
            if counter > 7:
                counter = 1
                base += 1

            ans += base + counter
            counter += 1

        return ans