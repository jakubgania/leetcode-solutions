# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums_arr = []
        
        def inorderTraversal(root):
            if root:
                inorderTraversal(root.left)
                nums_arr.append(root.val)
                inorderTraversal(root.right)

        def buildBST(nums):
            if not nums:
                return None

            k = len(nums) // 2
            new_root = TreeNode(nums[k])
            new_root.left = buildBST(nums[:k])
            new_root.right = buildBST(nums[k+1:])
            
            return new_root
        
        inorderTraversal(root)

        return buildBST(nums_arr)