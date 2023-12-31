# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_tree = self.curr = TreeNode()
        
        def postorder(root):
            if root == None:
                return

            postorder(root.left)

            self.curr.right = TreeNode(root.val)
            self.curr = self.curr.right

            postorder(root.right)

        postorder(root)
        return new_tree.right