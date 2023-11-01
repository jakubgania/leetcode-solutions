# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0  

        if root is None:
            return

        node_stack = []
        node_stack.append(root)

        while (len(node_stack) > 0):
            node = node_stack.pop()

            if node.val >= low and node.val <= high:
                ans += node.val

            if node.right is not None:
                node_stack.append(node.right)

            if node.left is not None:
                node_stack.append(node.left)
                
        return ans