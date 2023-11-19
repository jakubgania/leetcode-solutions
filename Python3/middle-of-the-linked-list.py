# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        stack = head
        temp_arr = []

        while stack:
            node = stack
            temp_arr.append(node.val)
            stack = node.next

        counter = 0

        if len(temp_arr) % 2 == 0:
            counter = len(temp_arr) / 2
        else:
            counter = (len(temp_arr) // 2)

        stack = head
        index = 0
        
        while stack:
            node = stack
            if index == counter:
                return node
            stack = node.next
            index += 1