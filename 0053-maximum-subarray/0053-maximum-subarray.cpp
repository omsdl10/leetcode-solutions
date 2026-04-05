class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n=nums.size();
        int ans=0;
        int result=nums[0];
        for(int i=0;i<n;i++){
            ans+=nums[i];
            result=max(ans,result);
            if(ans<0){
                ans=0;
            }
        }
        return result;
    }
};