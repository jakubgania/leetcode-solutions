# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_arr, greater_arr, pivot_arr = [], [], []

        for num in nums:
            if num < pivot:
                smaller_arr.append(num)

            if num > pivot:
                greater_arr.append(num)

            if num == pivot:
                pivot_arr.append(num)

        return smaller_arr + pivot_arr + greater_arr