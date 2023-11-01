# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points_sorted = sorted(points, key=lambda x: x[0])
        diff_arr = [0] * (len(points) - 1)

        for index in range(len(points_sorted) - 1):
            diff_arr[index] = points_sorted[index + 1][0] - points_sorted[index][0]

        return max(diff_arr)