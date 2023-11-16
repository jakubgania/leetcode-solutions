# https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
        ans = 0
        red_bool = green_bool = blue_bool = False
        
        for index_1 in range(0, 10):
            for index_2 in range(0, len(rings), 2):
                if int(rings[index_2: index_2 + 2][1]) == index_1:
                    if rings[index_2: index_2 + 2][0] == "R":
                        red_bool = True
                    
                    if rings[index_2: index_2 + 2][0] == "G":
                        green_bool = True

                    if rings[index_2: index_2 + 2][0] == "B":
                        blue_bool = True

            if red_bool and green_bool and blue_bool:
                ans += 1

            red_bool = green_bool = blue_bool = False

        return ans