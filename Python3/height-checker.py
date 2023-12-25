# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans, heights_sorted = 0, sorted(heights)

        for x, y in zip(heights_sorted, heights):
            if x != y:
                ans += 1

        return ans