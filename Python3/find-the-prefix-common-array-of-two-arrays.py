# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        temp, ans, counter = [], [None] * len(A), 0

        for index in range(0, len(A)):
            counter = 0
            temp.append(A[index])
            temp.append(B[index])

            for item in A[0:index + 1]:
                if temp.count(item) == 2:
                    counter += 1
            
            ans[index] = counter

        return ans