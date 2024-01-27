# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numbers_dict = defaultdict(int)
        occurrences_dict = defaultdict(int)

        for number in arr:
            numbers_dict[number] += 1

        for key in numbers_dict:
            occurrences_dict[numbers_dict[key]] += 1
            if occurrences_dict[numbers_dict[key]] == 2:
                return False

        return True