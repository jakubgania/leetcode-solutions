# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for index in range(m + n):
            if len(nums2) and nums1[index] == 0:
                nums1[index] = nums2.pop(0)

        for i in range(m + n):
            for j in range(0, m + n - i - 1 ):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]