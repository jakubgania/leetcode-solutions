# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        temp_arr, ans = [], []

        while nums:
            temp_arr += list(dict.fromkeys(nums))
            ans.append(temp_arr)

            for index in range(len(temp_arr)):
                nums.remove(temp_arr[index])
            
            temp_arr = []
        
        return ans