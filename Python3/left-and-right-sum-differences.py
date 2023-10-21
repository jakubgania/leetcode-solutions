# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans, left, right = [], [], []

        if len(nums) == 1:
            ans.append(0)
            return ans

        left.append(0)
        left += self.sumNumbers(nums)

        reversed_nums = list(reversed(nums))

        right += self.sumNumbers(reversed_nums)
        right = list(reversed(right))
        right.append(0)

        for index in range(len(nums)):
            val = abs(left[index] - right[index])
            ans.append(val)

        return ans

    def sumNumbers(self, arr) -> List[int]:
        resp, temp, counter = [], 0, 0
       
        for index in arr:
            if counter == len(arr) - 1:
                break
            else:
                temp += index
                resp.append(temp)
                counter += 1

        return resp
        