# https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans, words_len = 0, len(words)

        for index_1 in range(0, words_len - 1):
            for index_2 in range(index_1 + 1, words_len):
                if words[index_1] == words[index_2] or words[index_1] == words[index_2][::-1]:
                    ans += 1

        return ans