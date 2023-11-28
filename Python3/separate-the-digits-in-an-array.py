# https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []

        for item in nums:
            temp = str(item)
            for number in temp:
                arr.append(int(number))

        return arr