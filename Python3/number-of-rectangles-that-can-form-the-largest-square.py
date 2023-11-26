# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp_arr = []

        for item in rectangles:
            temp_arr.append(min(item[0], item[1]))

        return temp_arr.count(max(set(temp_arr)))