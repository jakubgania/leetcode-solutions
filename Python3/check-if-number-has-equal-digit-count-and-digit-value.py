# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    def digitCount(self, num: str) -> bool:
        flag = True

        for index in range(len(num)):
            if num.count(str(index)) != int(num[index]):
                flag = False

        return flag