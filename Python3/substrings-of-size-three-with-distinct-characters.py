# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0

        for index in range(len(s) - 2):
            if s[index] != s[index + 1] and s[index + 1] != s[index + 2] and s[index] != s[index + 2]:
                ans += 1
        
        return ans