# https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans, arr_len = 0, len(arr)

        for i in range(arr_len):
            for j in range(i + 1, arr_len):
                for k in range(j + 1, arr_len):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1

        return ans