# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for index in range(1, len(arr) - 1):
            if (arr[index + 1] - arr[index]) != diff:
                return False

        return True