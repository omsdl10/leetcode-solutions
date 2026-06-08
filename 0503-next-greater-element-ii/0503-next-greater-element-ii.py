class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2=nums+nums
        ans=[-1]*len(nums2)
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(nums2[i])
        return ans[:len(nums)]