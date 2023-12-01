# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        string_list = list(set(s))
        temp = s.count(string_list[0])

        for item in string_list[1:]: 
            if s.count(item) != temp:
                return False

        return True