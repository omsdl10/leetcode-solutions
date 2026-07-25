class Solution:
    def maxProduct(self, n: int) -> int:
        new=str(n)
        arr=[]
        for i in new:
            arr.append(int(i))
        arr.sort()
        return arr[-1]*arr[-2]