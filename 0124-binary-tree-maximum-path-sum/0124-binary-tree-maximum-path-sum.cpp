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
public:
    int maxsum(TreeNode* root,int& maximum){
        if(root==NULL){
            return 0;
        }
        int leftsum=max(0,maxsum(root->left,maximum));
        int rightsum=max(0,maxsum(root->right,maximum));
        maximum=max(maximum,root->val+leftsum+rightsum);
        return root->val+max(leftsum,rightsum);
    }
    int maxPathSum(TreeNode* root) {
        int maximum=INT_MIN;
        if(root==NULL){
            return maximum;
        }
        maxsum(root,maximum);
        return maximum;
    }
};