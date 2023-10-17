# https://leetcode.com/problems/root-equals-sum-of-children/

# without this it doesn't work locally in VSC
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val + root.right.val == root.val
        
# Input: root = [10,4,6]
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

solution = Solution()
print(solution.checkTree(root))

# expected output
# Output: true