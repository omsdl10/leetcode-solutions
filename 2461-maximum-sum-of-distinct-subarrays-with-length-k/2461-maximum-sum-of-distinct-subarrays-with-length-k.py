class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        maxsum=0
        l=0
        windowsum=0
        for r in range(len(nums)):
            windowsum+=nums[r]
            if nums[r] not in freq:
                freq[nums[r]]=1
            else:
                freq[nums[r]]+=1
            if r-l+1>k:
                freq[nums[l]]-=1
                windowsum-=nums[l]
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1
            if (r-l+1)==k and len(freq)==k:
                maxsum=max(maxsum,windowsum)
        return maxsum
        

