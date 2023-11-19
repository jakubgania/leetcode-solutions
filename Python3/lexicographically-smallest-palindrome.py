# https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_len = len(s)
        
        for index in range(s_len // 2):
            temp_index = s_len - 1 - index
            if s[index] != s[temp_index]:
                if ord(s[index]) > ord(s[temp_index]):
                    s = s[:index] + s[temp_index] + s[index + 1:]
                else:
                    s = s[:temp_index] + s[index] + s[temp_index + 1:]

        return s