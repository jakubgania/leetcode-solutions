# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s_len = len(s)

        for index in range(s_len // 2):
            s[index], s[s_len - 1 - index] = s[s_len - 1 - index], s[index]