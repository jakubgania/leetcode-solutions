# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            prefix = word[0:word.find(ch) + 1]
            return word.replace(prefix, prefix[::-1])
        
        return word
        