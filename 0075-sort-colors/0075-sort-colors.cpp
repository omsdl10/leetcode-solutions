class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zeros=0;
        int ones=0;
        int twos=0;
        
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0)zeros++;
            else if(nums[i]==1)ones++;
            else{
                twos++;
            }
        }
        int j=0;
        for(int i=0;i<zeros;i++){
            nums[j]=0;
            j++;
        }
        for(int i=0;i<ones;i++){
            nums[j]=1;
            j++;
        }
        for(int i=0;i<twos;i++){
            nums[j]=2;
            j++;
        }
    }
};