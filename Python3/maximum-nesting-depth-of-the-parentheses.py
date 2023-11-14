# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        ans, counter = 0, 0

        for item in s:
            if item == "(":
                counter += 1

            if item == ")":
                counter -= 1

            if counter > ans:
                ans = counter

        return ans