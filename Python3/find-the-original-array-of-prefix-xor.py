# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]

        for index in range(len(pref) - 1):
            ans.append(pref[index] ^ pref[index + 1])

        return ans