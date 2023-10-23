# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp_arr = [0] * len(s)

        for index in range(len(s)):
            temp_arr[indices[index]] = s[index]

        return "".join(temp_arr)