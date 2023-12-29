# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x = -1

        for index in range(len(arr) - 1, -1, -1):
            if arr[index] > x:
                x, arr[index] = arr[index], x
            else:
                arr[index] = x
        
        return arr