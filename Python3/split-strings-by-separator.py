# https://leetcode.com/problems/split-strings-by-separator/

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []

        for item in words:
            temp = [i for i in item.split(separator) if i]
            ans.extend(temp)

        return ans