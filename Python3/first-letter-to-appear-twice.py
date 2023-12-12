# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters_set = set()

        for item in s:
            if item in letters_set:
                return item
            else:
                letters_set.add(item)