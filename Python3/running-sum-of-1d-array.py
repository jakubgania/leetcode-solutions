# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        temp = 0
        
        for index in range(len(nums)):
            if index == 0:
                ans.append(nums[index])
                continue
            else:
                counter = 0
                temp = 0
                for number in nums:
                    temp += number
                    if counter == index:
                        break
                    
                    counter += 1

                ans.append(temp)

        return ans