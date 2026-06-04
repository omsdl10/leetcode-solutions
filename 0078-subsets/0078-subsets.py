def helper(i,arr,result,n,lis):
    if i>=n:
        result.append(lis[:])
        return
    
    helper(i+1,arr,result,n,lis)
    lis.append(arr[i])
    helper(i+1,arr,result,n,lis)
    lis.pop()


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        helper(0,nums,result,n,[])
        return result