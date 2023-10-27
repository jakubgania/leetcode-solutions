# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, s: str) -> str:
        counter, temp_arr = 0, [0] * len(s)

        for item in s:
            ascii_val = ord(item)

            if 65 <= ascii_val <= 90:
                temp_arr[counter] = ascii_val + 32
            else:
                temp_arr[counter] = ascii_val

            counter+= 1

        return "".join(chr(i) for i in temp_arr)