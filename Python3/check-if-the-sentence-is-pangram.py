# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = string.ascii_lowercase

        for item in alphabet:
            if item not in sentence:
                return False
        
        return True