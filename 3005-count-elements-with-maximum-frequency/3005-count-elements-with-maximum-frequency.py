class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap={}
        count=0
        freq=0
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        max_freq=max(hmap.values())
        for i in hmap:
            if hmap[i]==max_freq:
                count+=hmap[i]
        return count