class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0;
        int r=height.size()-1;
        long long ans=0;
        while(l<r){
            long long minheight=min(height[l],height[r]);
            long long width=r-l;
            ans=max(ans,minheight*width);
            if(height[l]<height[r])l++;
            else r--;
        }
        return ans;
    }
};