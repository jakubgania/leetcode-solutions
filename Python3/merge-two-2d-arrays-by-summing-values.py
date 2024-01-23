# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        x, y = 0, 0

        while x < len(nums1) and y < len(nums2):
            item1 = nums1[x][0]
            item2 = nums2[y][0]

            if item1 == item2:
                nums1[x][-1] += nums2[y][-1]
                ans.append(nums1[x])
                x += 1
                y += 1
            elif item1 < item2:
                ans.append(nums1[x])
                x += 1
            else:
                ans.append(nums2[y])
                y += 1

        ans.extend(nums1[x:])
        ans.extend(nums2[y:])

        return ans