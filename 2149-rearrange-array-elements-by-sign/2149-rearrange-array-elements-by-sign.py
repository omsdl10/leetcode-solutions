class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        i=0
        while i<len(pos):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
            i+=1 
        return nums