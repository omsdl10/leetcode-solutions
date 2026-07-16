class Solution {
public:
    int minCut(string A) {
       int n = A.size();
    if (n <= 1) return 0;
    
    // isPalin[i][j] = true if A[i..j] is a palindrome
    vector<vector<bool>> isPalin(n, vector<bool>(n, false));
    
    for (int i = 0; i < n; i++) isPalin[i][i] = true;
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            if (A[i] == A[j]) {
                if (len == 2 || isPalin[i+1][j-1])
                    isPalin[i][j] = true;
            }
        }
    }
    
    // dp[i] = min cuts needed for A[0..i]
    vector<int> dp(n, 0);
    
    for (int i = 0; i < n; i++) {
        if (isPalin[0][i]) {
            dp[i] = 0;
        } else {
            dp[i] = INT_MAX;
            for (int j = 0; j < i; j++) {
                if (isPalin[j+1][i] && dp[j] != INT_MAX) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
    }
    
    return dp[n-1]; 
    }
};