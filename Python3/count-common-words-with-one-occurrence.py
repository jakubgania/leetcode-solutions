# https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans, words1_dict, words2_dict = 0, {}, {}

        def convert(words):
            new_dict = {}

            for i in words:
                if i not in new_dict:
                    new_dict[i] = 1
                else:
                    new_dict[i] += 1

            return new_dict

        words1_dict = convert(words1)
        words2_dict = convert(words2)

        for i in words1_dict.keys():
            if words1_dict[i] == 1 and i in words2_dict and words2_dict[i] == 1:
                ans += 1

        return ans