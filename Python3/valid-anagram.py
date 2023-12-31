# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_s = Counter(s)
        word_t = Counter(t)
        
        if word_s == word_t:
            return True

        return False