# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        node_stack_p = []
        node_stack_q = []
        node_stack_p.append(p)
        node_stack_q.append(q)

        while node_stack_p:
            node_p = node_stack_p.pop(0)
            node_q = node_stack_q.pop(0)

            if node_p == None or node_q == None:
                return False

            if node_p != None and node_q != None and node_p.val != node_q.val:
                return False

            if (node_p != None and node_q != None) and (node_p.right is not None and node_q.right is not None):
                node_stack_p.append(node_p.right)
                node_stack_q.append(node_q.right)
            elif (node_p != None and node_q != None) and (node_p.right != node_q.right):
                return False

            if (node_p != None and node_q != None) and (node_p.left is not None and node_q.left is not None):
                node_stack_p.append(node_p.left)
                node_stack_q.append(node_q.left)
            elif (node_p != None and node_q != None) and (node_p.left != node_q.left):
                return False
        
        return True