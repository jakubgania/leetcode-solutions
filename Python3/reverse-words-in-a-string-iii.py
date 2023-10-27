# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        temp_arr = s.split(" ")

        return " ".join((temp_arr[key][::-1] for key in range(len(temp_arr))))