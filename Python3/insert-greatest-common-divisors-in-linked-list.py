# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head

        current=head

        while current:
            if current.next is not None:
                item=gcd(current.val, current.next.val)
                current.next = ListNode(item, current.next)
                current = current.next

            current = current.next
        
        return head

    # greatest common divisor algorithm
    def gcd(a, b):
        while b != 0:
            t = b
            b = a % b
            a = t

        return a