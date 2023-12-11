# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels_list = ['a', 'e', 'i', 'o', 'u']
        ans = 0

        for index in range(left, right + 1):
            if len(words[index]) > 1:
                temp_flag = True

                if words[index][0] not in vowels_list:
                    temp_flag = False

                if words[index][-1] not in vowels_list:
                    temp_flag = False
                
                if temp_flag:
                    ans += 1

            else:
                if words[index] in vowels_list:
                    ans += 1

        return ans