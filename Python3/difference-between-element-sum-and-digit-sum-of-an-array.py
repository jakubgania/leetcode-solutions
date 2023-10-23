# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        nums_sum, digits_sum = 0, 0

        for number in nums:
            nums_sum += number

            if number > 9:
                for item in range(len(str(number))):
                    digits_sum += self.getDigit(number, item)
            else:
                digits_sum += self.getDigit(number, 0)

        return abs(nums_sum - digits_sum)
    
    def getDigit(self, number, n) -> int:
        return number // 10**n % 10
        