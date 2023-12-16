# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for index in range(len(words)):
            if x in words[index]:
                ans.append(index)

        return ans