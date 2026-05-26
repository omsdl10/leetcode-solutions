class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Hmap={}
        n=(len(nums)/2)
        for i in nums:
            if i in Hmap:
                Hmap[i]+=1
            else:
                Hmap[i]=1
        for x, y in Hmap.items():
            if y>=n:
                return x
  
