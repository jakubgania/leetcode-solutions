# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0

        for item in text.split():
            flag = True
            for item_2 in brokenLetters:
                if item_2 in item:
                    flag = False
                    break
            if flag:
                ans += 1

        return ans