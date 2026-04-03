class Solution {
public:
    void dfs(TreeNode* root, int col, int row, map<int,vector<pair<int,int>>>& hmap){
        if(!root) return;

        hmap[col].push_back({row, root->val});

        dfs(root->left, col - 1, row + 1, hmap);
        dfs(root->right, col + 1, row + 1, hmap);
    }

    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;
        map<int,vector<pair<int,int>>> hmap;

        dfs(root, 0, 0, hmap); 

        for(auto &it : hmap) {
            auto vec = it.second;

            sort(vec.begin(), vec.end());

            vector<int> col;
            for(auto &p : vec) {
                col.push_back(p.second);
            }

            ans.push_back(col);
        }

        return ans;
    }
};