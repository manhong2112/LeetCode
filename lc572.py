# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def toStr(t):
            if t:
                return "({} {} {})".format(t.val, toStr(t.left), toStr(t.right))
            else:
                return ""
        return toStr(t) in toStr(s)