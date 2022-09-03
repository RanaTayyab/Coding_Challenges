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

        # BFS: keep removing parent from queue and keep adding left and right child and at the end of inner loop increase the level by 1; two loops: one for queue length > 0 and inner loop is for traversing everything in that particular level on elements in the queue

        while len(q) > 0:

            for i in range(len(q)):

                root = q.popleft()

                if root.left:
                    q.append(root.left)

                if root.right:
                    q.append(root.right)

            depth += 1

        return depth
