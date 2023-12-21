# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_values = []
        
        if root is None:
            return

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            node_values.append(node.val)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        node_values.sort()
        max_value = max(node_values)
    
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            node_index = node_values.index(node.val)

            if node.val < max_value:
                node.val = sum(node_values[node_index:])

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return root