# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, temp_arr = 0, []

        for item in bank:
            if item.count("1") > 0:
                temp_arr.append(item.count("1"))

        for index in range(len(temp_arr) - 1):
            ans += temp_arr[index] * temp_arr[index + 1]

        return ans