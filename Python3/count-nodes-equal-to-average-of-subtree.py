# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
            
        def count_nodes(root):
            if root == None:
                return 0

            return 1 + count_nodes(root.left) + count_nodes(root.right)

        def sum_nodes(root):
            if root == None:
                return 0

            return root.val + sum_nodes(root.left) + sum_nodes(root.right)

        def preorder(root):
            if root == None:
                return 0

            if root.val == (sum_nodes(root) // count_nodes(root)):
                return 1 + preorder(root.left) + preorder(root.right)
            else:
                return preorder(root.left) + preorder(root.right)

        return preorder(root)