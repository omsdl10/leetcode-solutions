class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        if(root == NULL) return ans;

        queue<TreeNode*> q;
        q.push(root);

        while(!q.empty()){
            int len = q.size();
            long long addtion = 0;

            for(int i = 0; i < len; i++){
                TreeNode* node = q.front();
                q.pop();

                addtion += node->val;

                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }

            ans.push_back((double)addtion / len);
        }

        return ans;
    }
};