/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#define NULLSAFE_ACC_MEMBER(PTR,MEM,VAL) (((PTR)==NULL)?(VAL):(PTR)->MEM)
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(t1 == t2 and t2 == NULL) {
            return NULL;
        } else {
            TreeNode* t = (TreeNode*) malloc(sizeof(TreeNode));
            t->val = NULLSAFE_ACC_MEMBER(t1, val, 0) + NULLSAFE_ACC_MEMBER(t2, val, 0);
            t->left = mergeTrees(NULLSAFE_ACC_MEMBER(t1, left, NULL), NULLSAFE_ACC_MEMBER(t2, left, NULL));
            t->right = mergeTrees(NULLSAFE_ACC_MEMBER(t1, right, NULL), NULLSAFE_ACC_MEMBER(t2, right, NULL));
            return t;
        }
    }

};