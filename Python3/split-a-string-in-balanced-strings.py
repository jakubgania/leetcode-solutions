# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans, counter = 0, 0

        for item in s:
            if item == "L":
                counter += 1
            else:
                counter -= 1

            if counter == 0:
                ans += 1
                counter = 0

        return ans