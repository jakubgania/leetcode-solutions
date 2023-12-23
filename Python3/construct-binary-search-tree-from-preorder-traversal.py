# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        index = 1

        while index < len(preorder) and preorder[index] < root.val:
            index += 1

        root.left = self.bstFromPreorder(preorder[1:index])
        root.right = self.bstFromPreorder(preorder[index:])

        return root