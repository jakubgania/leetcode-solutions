# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        ruleKeyToValue = {"type": 0, "color": 1, "name": 2}
        ruleKeyValue = ruleKeyToValue[ruleKey]

        for item in items:
            if item[ruleKeyValue] == ruleValue:
                ans += 1

        return ans