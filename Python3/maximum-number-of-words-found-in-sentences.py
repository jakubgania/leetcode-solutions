# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        temp = []
        
        for sentence in sentences:
            temp.append(len(sentence.split(" ")))

        return max(temp)