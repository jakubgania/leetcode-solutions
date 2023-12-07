# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        
        for index in range(n // 2):
            ans.append(index + 1)
            ans.append(0 - index - 1)

        if n % 2 != 0:
            ans.append(0)

        return ans