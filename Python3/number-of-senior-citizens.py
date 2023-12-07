# https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([1 for item in details if int(item[11:13]) > 60])