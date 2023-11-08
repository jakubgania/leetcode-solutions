# https://leetcode.com/problems/decode-the-message/

import base64

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ans = ""

        key = key.replace(" ", "")
        key = "".join(dict.fromkeys(key))
        alphabet = string.ascii_lowercase

        for item in message:
            if item.isspace() == True:
                ans += " "
            else:
                ans += alphabet[key.index(item)]

        return ans