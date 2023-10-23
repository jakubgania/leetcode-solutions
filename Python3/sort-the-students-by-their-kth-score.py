# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        dict, ans = {}, []

        for index in range(len(score)):
            dict[score[index][k]] = index

        dict_keys = list(dict.keys())
        dict_keys.sort(reverse=True)
        sorted_dict = {i: dict[i] for i in dict_keys}

        for value in sorted_dict.values():
            ans.append(score[value])

        return ans