class Solution {
public:
    int level(TreeNode* root, int value, int l){
        if(root == NULL) return -1;
        if(root->val == value) return l;

        int left = level(root->left, value, l + 1);
        if(left != -1) return left;

        return level(root->right, value, l + 1);
    }

    bool sibling(TreeNode* root, int x, int y){
        if(root == NULL) return false;

        if(root->left && root->right){
            if((root->left->val == x && root->right->val == y) ||
               (root->left->val == y && root->right->val == x)){
                return true;
            }
        }

        return sibling(root->left, x, y) || sibling(root->right, x, y);
    }

    bool isCousins(TreeNode* root, int x, int y) {
        if(root == NULL) return false;

        int lx = level(root, x, 0);
        int ly = level(root, y, 0);

        return (lx == ly) && !sibling(root, x, y);
    }
};