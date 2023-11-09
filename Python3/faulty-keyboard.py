# https://leetcode.com/problems/faulty-keyboard/

class Solution:
    def finalString(self, s: str) -> str:

        while s.find("i") > -1:
            t = s
            i_position = s.find("i")
            s = s[0:i_position][::-1].replace("i", "") + t[i_position + 1:]
        
        return s