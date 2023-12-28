# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        set_row_1 = set("qwertyuiop")
        set_row_2 = set("asdfghjkl")
        set_row_3 = set("zxcvbnm")

        for word in words:
          temp = set(word.lower())

          if temp <= set_row_1 or temp <= set_row_2 or temp <= set_row_3:
            ans.append(word)

        return ans