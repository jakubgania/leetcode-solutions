# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, counter, arr_len = 0, 0, len(arr)
        odd_numbers = [x for x in range(arr_len + 1) if x % 2 == 1]

        for item in odd_numbers:
            index = 0
            while item + index <= arr_len:
                ans += sum(arr[index:item + index])
                index += 1

        return ans