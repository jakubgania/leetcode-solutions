# https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for item in range(low, high + 1):
            item_str = str(item)
            item_str_len = len(item_str)

            if item_str_len % 2 == 0:
                temp_item_len = item_str_len // 2
                
                left = sum(int(x) for x in item_str[0:temp_item_len])
                right = sum(int(x) for x in item_str[temp_item_len:])
                
                if left == right:
                    ans += 1

        return ans