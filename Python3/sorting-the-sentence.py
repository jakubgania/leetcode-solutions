# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        temp_arr = s.split(" ")
        temp_arr_2 = [None] * len(temp_arr)

        for index in range(len(temp_arr)):
            temp_len = len(temp_arr[index]) - 1
            index_arr = int(temp_arr[index][temp_len])
            temp_arr_2[index_arr - 1] = temp_arr[index].replace(temp_arr[index][temp_len], "")

        return " ".join(temp_arr_2)
        