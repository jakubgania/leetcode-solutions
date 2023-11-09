# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, temp = [0], 0

        for item in gain:
            temp = item + temp
            ans.append(temp)

        return max(ans)