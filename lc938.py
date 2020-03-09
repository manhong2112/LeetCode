# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        l, r = 0, 0
        if root.val >= L:
            l = self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            r = self.rangeSumBST(root.right, L, R)
        if L <= root.val <= R:
            return root.val + l + r
        else:
            return l + r
