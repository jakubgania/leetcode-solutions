# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans, temp_arr = [], []

        for index in range(len(l)):
            for index2 in range(l[index], r[index] + 1):
                temp_arr.append(nums[index2])

            temp_arr = sorted(temp_arr, reverse=True)
            
            if len(temp_arr) < 2:
                return ans.append(False)

            temp_val = abs(temp_arr[0]) - abs(temp_arr[1])
            
            for index in range(len(temp_arr)):
                if index + 1 < len(temp_arr) and abs(temp_arr[index]) - abs(temp_arr[index + 1]) != temp_val:
                    ans.append(False)
                    break

                if index + 1 == len(temp_arr):
                    ans.append(True)

            temp_arr = []

        return ans