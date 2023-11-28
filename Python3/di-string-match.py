# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = list(range(len(s) + 1))
        counter = -1
        index = 0

        while counter < (len(s) - 1):
            if s[index] == "I":
                if perm[index] < perm[index + 1]:
                    counter += 1
                else:
                    counter -= 1
                    perm[index], perm[index + 1] = perm[index + 1], perm[index]

            if s[index] == "D":
                if perm[index] > perm[index + 1]:
                    counter += 1
                else:
                    counter -= 1
                    perm[index], perm[index + 1] = perm[index + 1], perm[index]

            if index == (len(s) - 1):
                index = 0
                counter = 0
            else:
                index += 1

        return perm