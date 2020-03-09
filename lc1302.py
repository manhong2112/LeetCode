# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q1 = [root]
        q2 = []
        deepest = []
        while q1 or q2:
            while q1:
                n = q1.pop()
                if n.left:
                    q2.append(n.left)
                if n.right:
                    q2.append(n.right)
            if not q2:
                return sum(i.val for i in deepest)
            deepest = list(q2)
            q1 = q2
            q2 = []
        