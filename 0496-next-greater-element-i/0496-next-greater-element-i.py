class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums2)
        stack=[]
        res=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    res.append(ans[j])
        return res


        

        
            
