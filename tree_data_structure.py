class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        print("root value: ")

        print(root.val)

        left_depth = self.maxDepth(root.left)

        print("root value: ")

        print(root.val)

        print("left depth: ")
        print(left_depth)


        right_depth = self.maxDepth(root.right)

        print("root value: ")
        print(root.val)

        print("right depth: ")
        print(right_depth)


        maximum = max(left_depth, right_depth)

        max_and_root = 1 + maximum


        print("max and root: ")
        print(max_and_root)

        return max_and_root


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left=node4
node3.right=node5


S = Solution()

depth = S.maxDepth(node1)

print(depth)