# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        alphabet = string.ascii_uppercase
        cells = s.split(":")
        letter_start = cells[0][:1]
        letter_end = cells[1][:1]
        start_number = int(cells[0][1:])
        end_number = int(cells[1][1:])

        for index_1 in range(alphabet.index(letter_start), alphabet.index(letter_end) + 1):
            for index_2 in range(start_number, end_number + 1):
                ans.append(alphabet[index_1] + str(index_2))

        return ans