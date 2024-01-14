# https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree_node_values = 0

        def greaterTree(node):
            nonlocal tree_node_values

            if node:
                greaterTree(node.right)
                node.val += tree_node_values
                tree_node_values = node.val
                greaterTree(node.left)
            
            return node
        
        return greaterTree(root)