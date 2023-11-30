# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        chars_arr = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

        if sum((chars_arr[coordinates[0]], int(coordinates[1]))) % 2 == 0:
            return False
        
        return True