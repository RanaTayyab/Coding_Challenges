# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        from collections import deque

        depth = 0

        if root is None:
            return depth

        q = deque()

        q.append(root)

        while len(q) > 0:

            # inner loop is dealing with all the children of one parent node

            for i in range(len(q)):

                root = q.popleft()

                if root.left:
                    q.append(root.left)

                if root.right:
                    q.append(root.right)

            depth += 1

        return depth
