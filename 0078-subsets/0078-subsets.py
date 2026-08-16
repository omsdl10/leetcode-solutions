def helper(arr,n,ls,array):
    if n==len(arr):
        array.append(ls.copy())
        return 
    ls.append(arr[n])
    helper(arr,n+1,ls,array)
    ls.pop()
    helper(arr,n+1,ls,array)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        array=[]
        helper(nums,0,[],array)
        return array