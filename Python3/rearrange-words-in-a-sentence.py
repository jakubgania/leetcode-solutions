# https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution:
    def arrangeWords(self, text: str) -> str:
        words, ans = {}, ""
        text = text.split(" ")

        for item in text:
            if words.get(len(item)) is not None:
                words[len(item)] = words[len(item)] + " " + item
            else:
                words[len(item)] = item

        ans = " ".join((words[key] for key in sorted(words.keys())))

        return ans.lower().capitalize()