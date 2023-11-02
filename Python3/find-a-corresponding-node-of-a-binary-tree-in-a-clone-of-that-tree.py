# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        node_stack = []
        node_stack.append(cloned)

        while node_stack:
            node = node_stack.pop(0)

            if node.val == target.val:
                return node

            if node.right is not None:
                node_stack.append(node.right)

            if node.left is not None:
                node_stack.append(node.left)