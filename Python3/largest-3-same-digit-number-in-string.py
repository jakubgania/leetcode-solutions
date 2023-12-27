# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans, temp_list = 0, []

        for index in range(len(num) - 2):
            if (num[index] == num[index + 1] and
                num[index + 1] == num[index + 2] and
                num[index + 2] == num[index]):
                temp = num[index] * 3
                temp_list.append(temp)

        if len(temp_list):
            temp_list = sorted(temp_list, reverse=True)
 
            return temp_list[0]

        return ""