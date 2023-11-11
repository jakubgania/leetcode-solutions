# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha_arr = string.ascii_lowercase
        alpha_dict = {}
        ans = ""

        for index in range(26):
            if 1 <= index + 1 <= 9:
                alpha_dict[str(index + 1)] = alpha_arr[index]
            else:
                alpha_dict[str(index + 1) + "#"] = alpha_arr[index]

        while s:
            if s[-1:] == "#":
                ans += alpha_dict[s[-3:]]
                s = s[:-3]
            else:
                ans += alpha_dict[s[-1:]]
                s = s[:-1]

        return ans[::-1]