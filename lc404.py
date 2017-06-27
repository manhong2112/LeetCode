# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return (root.left.val if root.left and not root.left.left and not root.left.right else 0) + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        else:
            return 0