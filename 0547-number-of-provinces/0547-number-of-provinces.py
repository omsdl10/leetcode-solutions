class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        answer=0
        def dfs(city):
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and not visited[neighbour]:
                    visited[neighbour]=True
                    dfs(neighbour)
        for i in range(len(visited)):
            if not visited[i]:
                visited[i]=True
                dfs(i)
                answer+=1
        return answer