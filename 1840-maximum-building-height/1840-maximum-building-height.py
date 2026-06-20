class Solution:
    def maxBuilding(self,n:int,restrictions:List[List[int]])->int:
        restrictions.append([1,0])
        restrictions.append([n,n-1])
        restrictions.sort()
        for i in range(1,len(restrictions)):
            dist=restrictions[i][0]-restrictions[i-1][0]
            restrictions[i][1]=min(restrictions[i][1],restrictions[i-1][1]+dist)
        for i in range(len(restrictions)-2,-1,-1):
            dist=restrictions[i+1][0]-restrictions[i][0]
            restrictions[i][1]=min(restrictions[i][1],restrictions[i+1][1]+dist)
        ans=0
        for i in range(1,len(restrictions)):
            id1,h1=restrictions[i-1]
            id2,h2=restrictions[i]
            dist=id2-id1
            ans=max(ans,(h1+h2+dist)//2)

        return ans