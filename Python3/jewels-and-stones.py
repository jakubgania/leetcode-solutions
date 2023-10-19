# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum=0
        stones_array=[]
        jewels_array=[]

        for letter in stones:
            stones_array.append(letter)

        for letter in jewels:
            jewels_array.append(letter)

        for index in range(len(jewels_array)):
            sum += stones_array.count(jewels_array[index])

        return sum 