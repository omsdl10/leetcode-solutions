def helper(arr,n,ls,result):
    if n==len(arr):
        result.append(ls[:])
        return
    ls.append(arr[n])
    helper(arr,n+1,ls,result)
    while n+1<len(arr) and arr[n]==arr[n+1]:
        n+=1
    ls.pop()
    helper(arr,n+1,ls,result)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        helper(nums,0,[],result)
        return result