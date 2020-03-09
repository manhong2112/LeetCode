# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode, p=1, gp=1) -> int:
        if root is None:
            return 0
        if gp % 2 == 0:
            return root.val + self.sumEvenGrandparent(root.left, root.val, p) + self.sumEvenGrandparent(root.right, root.val, p)
        else:
            return self.sumEvenGrandparent(root.left, root.val, p) + self.sumEvenGrandparent(root.right, root.val, p)
