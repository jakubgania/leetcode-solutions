# https://leetcode.com/problems/merge-similar-items/

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ans = []
        items = items1 + items2
        items_dict = defaultdict(int)

        for index in items:
            value, weight = index
            items_dict[value] = items_dict[value] + weight

        for index in sorted(items_dict):
            ans.append([index, items_dict[index]])

        return ans