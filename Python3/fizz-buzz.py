# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for index in range(1, n + 1):
            if (index % 3 == 0 and index % 5 == 0):
                ans.append("FizzBuzz")
            elif (index % 3 == 0):
                ans.append("Fizz")
            elif (index % 5 == 0):
                ans.append("Buzz")
            else:
                ans.append(str(index))

        return ans