# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ans=1
        sum=0
        x=map(int,str(n))

        for number in x:
            ans = ans * number
            sum += number
            print(sum)
        
        return ans - sum