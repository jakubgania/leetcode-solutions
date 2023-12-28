# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans, trees = [], [root1, root2]

        def printInorder(root):
            if root:
                printInorder(root.left)
                ans.append(root.val)
                printInorder(root.right)

        for item in trees:
            printInorder(item)

        return sorted(ans)