# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr_1 = list(set(nums1) - set(nums2))
        arr_2 = list(set(nums2) - set(nums1))

        return [arr_1, arr_2]