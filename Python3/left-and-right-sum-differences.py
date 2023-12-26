# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans, left, right, nums_len = [], [], [], len(nums)

        if nums_len == 1:
            return [0]

        left.append(0)
        left.extend(self.sumNumbers(nums))

        reversed_nums = nums[::-1]

        right.extend(self.sumNumbers(reversed_nums))
        right = right[::-1]
        right.append(0)

        for index in range(nums_len):
            ans.append(abs(left[index] - right[index]))

        return ans

    def sumNumbers(self, arr) -> List[int]:
        resp, temp = [], 0

        for index in range(len(arr) - 1):
            temp += arr[index]
            resp.append(temp)

        return resp