# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution:
    def addMinimum(self, word: str) -> int:
        ans, index, counter, x = 0, 0, 0, "abc"
        
        while counter < len(word):
            if index == 3:
                index = 0
            
            if word[counter] == x[index]:
                counter += 1
            else:
                ans += 1
            
            index += 1

        return ans + 3 - index