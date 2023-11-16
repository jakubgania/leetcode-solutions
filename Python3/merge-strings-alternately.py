# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        for index in range(0, min(len(word1), len(word2))):
            ans += word1[index]
            ans += word2[index]

        ans += word1[index + 1:]
        ans += word2[index + 1:]

        return ans