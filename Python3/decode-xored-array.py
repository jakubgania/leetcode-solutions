# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        counter = 0

        for number in encoded:
            ans.append(ans[counter]^number)
            counter += 1

        return ans
        