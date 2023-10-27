# https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans, arr = [], {}

        for index in range(len(names)):
            arr[heights[index]] = names[index]

        for key in sorted(arr.keys(), reverse=True):
            ans.append(arr[key])

        return ans