# https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabet = string.ascii_lowercase

        for index in range(0, len(s) - 1, 2):
            s = s.replace(s[index + 1], alphabet[alphabet.find(s[index]) + int(s[index + 1])], 1)

        return s