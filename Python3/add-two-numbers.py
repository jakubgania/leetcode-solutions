# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_str_1, num_str_2, num_str_3 = "", "", ""

        def get_items(node):
            temp = ""
            curr = node

            while curr is not None:
                temp += str(curr.val)
                curr = curr.next

            return temp[::-1]

        num_str_1 = get_items(l1)
        num_str_2 = get_items(l2)
        num_str_3 = str(int(num_str_1) + int(num_str_2))
        num_str_3 = num_str_3[::-1]

        def create_linked_list(input_nums_as_str):
            counter = -1

            if input_nums_as_str:
                counter += 1
                return ListNode(int(input_nums_as_str[counter]), create_linked_list(input_nums_as_str[1:]))

        return create_linked_list(num_str_3)