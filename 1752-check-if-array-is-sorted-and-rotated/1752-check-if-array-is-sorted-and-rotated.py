def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
class Solution:
    def check(self, nums: List[int]) -> bool:

        sortarr=sorted(nums)
        for i in range(len(sortarr)):
            reverse(sortarr,0,len(sortarr)-1)
            reverse(sortarr,0,len(sortarr)-2)
            if sortarr==nums:
                return True
        return False