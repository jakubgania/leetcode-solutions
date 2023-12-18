# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return

        stack = []
        stack.append(root)
        temp = root.val

        while stack:

            node = stack.pop()

            if node.val != temp:
                return False

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return True