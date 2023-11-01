# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, temp_arr = [], []

        if not root:
            return []
        
        node_stack = []
        node_stack.append(root)

        while node_stack:
            size = len(node_stack)
            temp_stack = []

            while size > 0:
                node = node_stack.pop(0)
                temp_stack.append(node.val)
                size -= 1

                if node.left is not None:
                    node_stack.append(node.left)

                if node.right is not None:
                    node_stack.append(node.right)

            ans.append(temp_stack)

        return ans