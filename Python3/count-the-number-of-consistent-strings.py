# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter, flag = 0, False

        for item in words:
            for n in item:
                if n not in allowed:
                    flag = False
                    break
                else:
                    flag = True

            if flag:
                counter += 1
                flag = False

        return counter