# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        m = max(nums)
        k = nums.index(m)
        n = TreeNode(m)
        n.left = self.constructMaximumBinaryTree(nums[:k])
        n.right = self.constructMaximumBinaryTree(nums[k+1:])
        return n
