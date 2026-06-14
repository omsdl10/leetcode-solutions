def helper(arr, n):
    if arr[n] != -1:
        return arr[n]

    arr[n] = helper(arr, n-1) + helper(arr, n-2)
    return arr[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1] * (n + 1)

        arr[0] = 1
        arr[1] = 1

        return helper(arr, n)
