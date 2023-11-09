# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        ans, counter = 0, 1
        s = s.split("|")

        for item in s:
            if counter % 2 != 0 and item.count("*") > 0:
                ans += item.count("*")
            counter += 1

        return ans