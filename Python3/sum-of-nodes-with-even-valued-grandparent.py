# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        
        if root is None:
            return

        stack = []
        stack.append(root)

        while stack:

            node = stack.pop()

            if node.left is not None and node.val % 2 == 0:
                if node.left.left is not None:
                    ans += node.left.left.val

                if node.left.right is not None:
                    ans += node.left.right.val

            if node.right is not None and node.val % 2 == 0:
                if node.right.left is not None:
                    ans += node.right.left.val

                if node.right.right is not None:
                    ans += node.right.right.val

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return ans