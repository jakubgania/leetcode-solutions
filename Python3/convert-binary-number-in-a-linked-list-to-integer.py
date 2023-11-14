# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num, input_data = [], head

        while input_data:
            num.append(input_data.val)
            input_data = input_data.next

        num = "".join(map(str, num))
        
        return int(num, 2)