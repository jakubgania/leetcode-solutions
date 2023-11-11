# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, temp_arr = "", []
        right_bracket = left_bracket = counter = 0

        for item in s:
            if item == "(": left_bracket += 1
            if item == ")": right_bracket += 1
            
            counter += 1

            if left_bracket == right_bracket:
                temp_arr = s[0:counter]
                ans += temp_arr[1:len(temp_arr) - 1]
                s = s[counter:]
                
                right_bracket = left_bracket = counter = 0

        return ans