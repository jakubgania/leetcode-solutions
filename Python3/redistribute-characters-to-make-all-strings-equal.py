# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_counter_dict = {}
        num_words = len(words)

        for word in words:
            for char in word:
                char_counter_dict[char] = char_counter_dict.get(char, 0 ) + 1

        for count in char_counter_dict.values():
            if count % num_words != 0:
                return False

        return True        