# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root

        # If root is none then return root; otherwise swap nodes at same level and run root.left and root.right recursion and in the end return root

        if root is not None:
            root.left, root.right = root.right, root.left

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root


