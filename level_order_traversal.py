# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque

        if root is None:
            return root

        answer = []

        # Write BFS directly using two loops way and keep appending answers of each level of inner loop; in final answer of outer loop and return this answer

        if root is not None:

            q = deque()

            q.append(root)

            while len(q) > 0:

                temp_ans = []

                for i in range(len(q)):

                    root = q.popleft()

                    temp_ans.append(root.val)

                    if root.left:
                        q.append(root.left)

                    if root.right:
                        q.append(root.right)

                answer.append(temp_ans)

        return answer






