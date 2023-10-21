# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []

        for index in range(len(candies)):
            logical_flag = True
            for number in candies:
                if candies[index] == number:
                    continue
                elif candies[index] + extraCandies < number:
                    logical_flag = False
            
            ans.append(logical_flag)

        return ans