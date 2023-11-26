# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for item in words:
            item_reverse = item[::-1]
            if item == item_reverse:
                return item

        return ""