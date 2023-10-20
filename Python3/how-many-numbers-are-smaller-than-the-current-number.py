# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter=0
        temp=0
        ans=[]

        for index in range(len(nums)):
            temp=nums[index]

            # counter = sum(1 for i in nums if i < temp)

            for item in nums:
                if item < temp:
                   counter+= 1

            ans.append(counter)
            counter=0

        return ans