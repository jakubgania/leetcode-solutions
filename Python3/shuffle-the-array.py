# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        response = []
        x_1 = slice(0, n+1)
        x_2 = slice(n, 2*n)
        list_1 = nums[x_1]
        list_2 = nums[x_2]

        for index in range(n):
            response.append(list_1[index])
            response.append(list_2[index])

        return response