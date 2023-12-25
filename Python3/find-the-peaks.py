# https://leetcode.com/problems/find-the-peaks/

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []

        for index in range(1, len(mountain) - 1):
            if mountain[index] > mountain[index - 1] and mountain[index] > mountain[index + 1]:
                ans.append(index)

        return ans