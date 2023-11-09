# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0

        while n > 1:
            if n % 2 == 0:
                temp = int(n / 2)
                ans += temp
                n = n - temp
            else:
                temp = int((n - 1) / 2)
                ans += temp
                n = n - temp

        return ans