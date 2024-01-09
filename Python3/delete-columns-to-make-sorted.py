# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0

        for column in zip(*strs):
            if list(column) != sorted(column):
                ans += 1
        
        return ans