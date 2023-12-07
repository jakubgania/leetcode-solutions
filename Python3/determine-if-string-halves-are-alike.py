# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s_len = len(s) // 2
        first_half, second_half = s[:s_len], s[s_len:]
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        first_counter = 0
        second_counter = 0

        for x, y in zip(first_half, second_half):
            if x in vowels:
                first_counter += 1

            if y in vowels:
                second_counter += 1

        return first_counter == second_counter