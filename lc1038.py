# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def sumTree(n, k):
            if not n:
                return 0
            return ((n.val if n.val >= k else 0) + sumTree(n.left, k) + sumTree(n.right, k))

        def genTree(n):
            if not n:
                return None
            nn = TreeNode(sumTree(root, n.val))
            nn.left = genTree(n.left)
            nn.right = genTree(n.right)
            return nn

        return genTree(root)
