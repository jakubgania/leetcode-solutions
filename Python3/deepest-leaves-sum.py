# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        node_stack = []
        node_stack.append(root)

        deep_1 = 0

        while node_stack:
            x = len(node_stack)

            deep_1 += 1

            for i in range(x):
                node = node_stack.pop(0)

                if node.right is not None:
                    node_stack.append(node.right)

                if node.left is not None:
                    node_stack.append(node.left)

        node_stack_2 = []
        node_stack_2.append(root)

        deep_2 = 0

        while node_stack_2:
            x = len(node_stack_2)

            deep_2 += 1

            for i in range(x):
                node = node_stack_2.pop(0)

                if deep_1 == deep_2:
                    ans += node.val

                if node.right is not None:
                    node_stack_2.append(node.right)

                if node.left is not None:
                    node_stack_2.append(node.left)

        return ans