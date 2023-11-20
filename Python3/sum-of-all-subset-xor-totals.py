# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans, subsets = 0, [[]]
    
        for item in nums:
            for i in range(len(subsets)):
                subsets += [subsets[i]+[item]]
                if len(subsets[i]+[item]) == 1:
                    ans += item
                else:
                    temp_xor = 0
                    for x in subsets[i]+[item]:
                        temp_xor ^= x

                    ans += temp_xor

        return ans