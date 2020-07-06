class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            rt = root
            v = preorder[i]
            while True:
                if v > rt.val:
                    if rt.right:
                        rt = rt.right
                    else:
                        rt.right = TreeNode(v)
                        break
                else:
                    if rt.left:
                        rt = rt.left
                    else:
                        rt.left = TreeNode(v)
                        break
        return root
