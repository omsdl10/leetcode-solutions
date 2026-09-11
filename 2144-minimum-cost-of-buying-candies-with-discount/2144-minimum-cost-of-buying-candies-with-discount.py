class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        val=0
        point=2
        for i in range(len(cost)-1,-1,-1):
            if point==0:
                point=2
                continue
            else:
                val+=cost[i]
                point-=1
        return val