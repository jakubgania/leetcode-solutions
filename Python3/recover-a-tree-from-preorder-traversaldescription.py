# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        node_dict = {}
        dash_counter = 0
        counter = 0

        while counter < len(traversal):
            if traversal[counter] == "-":
                dash_counter += 1
                counter += 1
            else:
                number = ""

                while counter < len(traversal) and traversal[counter].isnumeric():
                    number += traversal[counter]
                    counter += 1

                number = int(number)

                node_dict[dash_counter] = TreeNode(number)

                if dash_counter - 1 in node_dict:
                    if not node_dict[dash_counter - 1].left:
                        node_dict[dash_counter - 1].left = node_dict[dash_counter]
                    else:
                        node_dict[dash_counter - 1].right = node_dict[dash_counter]

                dash_counter = 0

        return node_dict[0]