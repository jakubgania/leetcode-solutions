# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        values_without_duplicates = list(dict.fromkeys(groupSizes))
        ans = []

        for item in values_without_duplicates:
            temp = []
        
            for index in range(len(groupSizes)):
                if groupSizes[index] == item:
                    temp.append(index)
                
                if len(temp) == item:
                    ans.append(temp)
                    temp = []
                
        return ans