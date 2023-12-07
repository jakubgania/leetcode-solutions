# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_list, odd_list = [], []

        for item in nums:
            if item % 2 == 0:
                even_list.append(item)
            else:
                odd_list.append(item)

        return even_list + odd_list