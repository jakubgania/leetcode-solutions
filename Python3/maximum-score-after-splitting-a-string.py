# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0

        for index in range(len(s) - 1):
            left = s[0:index + 1]
            right = s[index + 1:]
            temp = left.count("0") + right.count("1")

            if temp > ans:
                ans = temp

        return ans 