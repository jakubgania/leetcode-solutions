# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0

        for item in words:
            if pref == item[0:len(pref)]:
                ans += 1

        return ans