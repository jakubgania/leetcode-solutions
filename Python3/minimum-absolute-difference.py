# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans, temp = [], []
        arr.sort()

        for index in range(len(arr) - 1):
            temp.append(abs(arr[index] - arr[index + 1]))

        minimum_diff = min(temp)

        for index in range(len(arr) - 1):
            if abs(arr[index] - arr[index + 1]) == minimum_diff:
                ans.append([arr[index], arr[index + 1]])

        return ans