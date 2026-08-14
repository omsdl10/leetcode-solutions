class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        sets=set()
        hmap={}
        nsq=len(grid)*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in hmap:
                    hmap[grid[i][j]]+=1
                else:
                    hmap[grid[i][j]]=1
                sets.add(grid[i][j])
        total=sum(sets)
        missing=(nsq*(nsq+1))//2-total
        repeated=0
        for key in hmap:
            if hmap[key]>1:
                repeated=key
        return [repeated,missing]