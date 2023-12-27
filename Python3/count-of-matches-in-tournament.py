# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans, temp = 0, 0

        while n > 1:
            if n % 2 == 0:
                temp = n // 2
            else:
                temp = (n - 1) // 2

            ans += temp
            n -= temp

        return ans