# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters_list = {"a": "0", "b": "1", "c": "2", "d": "3", "e": "4", "f": "5",
            "g": "6", "h": "7", "i": "8", "j": "9"}

        words_list = [firstWord, secondWord, targetWord]

        def convert(word):
            temp = ''.join([letters_list[item] for item in word])

            if len(temp) > 1:
                if len(temp) == temp.count("0"):
                    temp = "0"
                else:
                    temp = temp.lstrip("0")
            
            return int(temp)

        converted = list(map(convert, words_list))

        return converted[0] + converted[1] == converted[2]