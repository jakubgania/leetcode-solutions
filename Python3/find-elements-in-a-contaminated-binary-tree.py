# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.set = {0}
        self.root = root

        def dfs(root, val = 0):
            if root:
                if root.left:
                    root.left.val = 2 * val + 1
                    self.set.add(root.left.val)
                    dfs(root.left, root.left.val)

                if root.right:
                    root.right.val = 2 * val + 2
                    self.set.add(root.right.val)
                    dfs(root.right, root.right.val)

        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)