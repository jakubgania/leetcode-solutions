# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans, counter = [], 0

        for item in operations:
            if item.lstrip('-').isdigit():
                ans.append(int(item))
                counter += 1
            elif item == "C":
                ans.pop()
                counter -= 1
            elif item == "D":
                ans.append(ans[counter - 1] * 2)
                counter += 1
            elif item == "+":
                ans.append(ans[counter - 2] + ans[counter - 1])
                counter += 1

        return sum(ans)