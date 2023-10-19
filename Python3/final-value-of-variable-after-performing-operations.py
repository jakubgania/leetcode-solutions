# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counter = 0

        for index in range(len(operations)):
            if operations[index] == "++X" or operations[index] == "X++":
                counter += 1
            else:
                counter -= 1

        return counter