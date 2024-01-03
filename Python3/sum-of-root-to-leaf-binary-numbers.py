# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, temp):
            nonlocal ans

            if not root.left and not root.right:
                temp.append(str(root.val))
                ans += int("".join(temp), 2)

            if root.left:
                dfs(root.left, temp + [str(root.val)])
                
            if root.right:
                dfs(root.right, temp + [str(root.val)])

        dfs(root, [])

        return ans