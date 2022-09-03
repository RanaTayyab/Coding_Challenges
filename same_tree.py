# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        if p is None and q is not None:
            return False

        if p is not None and q is None:
            return False

        # Check for 4 cases for the nodes of both the trees; and detailed check on only that case where both are not null; and in that compare if their values are equal; if the values are also equal then traverse for p.left, q.left and p.right, q.right and check if both are being returned true; that means return true; else return false

        if p is not None and q is not None:

            if p.val == q.val:

                l = self.isSameTree(p.left, q.left)

                r = self.isSameTree(p.right, q.right)

                if l is True and r is True:
                    return True

            else:
                return False



