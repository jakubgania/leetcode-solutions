# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for item in range(left, right + 1):
            if "0" not in str(item):
                flag = True
                temp = item
                while item != 0:
                    x = item % 10
                    if temp % x != 0:
                        flag = False
                    item = item // 10
                if flag:
                    ans.append(temp)

        return ans