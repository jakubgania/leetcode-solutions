# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def postorder(node):
            left, right = False, False

            if node.left:
                left = postorder(node.left)

            if node.right:
                right = postorder(node.right)

            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return left or right
            else:
                return left and right

        return postorder(root)