/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    bool isSametree(TreeNode* rot, TreeNode* subRot) {
        if (rot == nullptr && subRot == nullptr) return true;
        if (rot == nullptr || subRot == nullptr) return false;
        if (rot->val != subRot->val) return false;

        return isSametree(rot->left, subRot->left) && isSametree(rot->right, subRot->right);
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr) return false;
        if (isSametree(root, subRoot)) return true;

        return isSubtree(root->right, subRoot) || isSubtree(root->left, subRoot);
    }
};
