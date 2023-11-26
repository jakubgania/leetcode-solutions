# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(len(points) - 1):
            diff_x = abs(points[i][0] - points[i + 1][0])
            diff_y = abs(points[i][1] - points[i + 1][1])
            ans += max(diff_x, diff_y) 

        return ans