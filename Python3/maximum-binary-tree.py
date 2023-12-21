# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def buildBST(nums):
            if not nums:
                return None

            max_item = max(nums)
            index_of_max_item = nums.index(max_item)

            root = TreeNode(max_item)
            root.left = buildBST(nums[0:index_of_max_item])
            root.right = buildBST(nums[index_of_max_item + 1:])

            return root

        return buildBST(nums)